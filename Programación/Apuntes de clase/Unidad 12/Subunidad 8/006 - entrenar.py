#!/usr/bin/env python3
import os
import torch
from datetime import datetime

from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
from peft import LoraConfig, get_peft_model

# ------------------------------------------------------------
# CONFIG
# ------------------------------------------------------------
# Hemos añadido 'outputs/' a la ruta para que encuentre el fichero
DATA_FILE = "outputs/004-preentrenamiento relleno.jsonl"  
MODEL_NAME = "Qwen/Qwen2.5-3B-Instruct" 
OUTPUT_DIR = "./qwen25-3b-jvc-lora"

MAX_LENGTH = 512 
NUM_EPOCHS = 3 
LR = 2e-4 
BATCH_SIZE = 1
GRAD_ACCUM = 4

def main():
    start_dt = datetime.now()

    print("🚀 Iniciando entrenamiento con Qwen2.5-3B-Instruct")
    print(f"📄 Dataset: {DATA_FILE}")
    print(f"🧠 Modelo base: {MODEL_NAME}")
    print("-" * 60)

    # ------------------------------------------------------------
    # Verificación del archivo
    # ------------------------------------------------------------
    if not os.path.isfile(DATA_FILE):
        print(f"❌ Error: No se encuentra el archivo en {DATA_FILE}")
        print("💡 Sugerencia: Asegúrate de que el archivo .jsonl esté dentro de la carpeta 'outputs'")
        return

    device = "cuda" if torch.cuda.is_available() else "cpu"
    if device == "cuda":
        print("💻 CUDA detectada. Usando GPU.")
    else:
        print("💻 No se detectó CUDA. Usando CPU (será lento).")

    # ------------------------------------------------------------
    # Carga de Tokenizer y Modelo
    # ------------------------------------------------------------
    print("✅ Cargando tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    print("✅ Cargando modelo base...")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.float16 if device == "cuda" else torch.float32,
        device_map="auto" if device == "cuda" else None,
    )

    # ------------------------------------------------------------
    # Configuración de LoRA
    # ------------------------------------------------------------
    print("✅ Aplicando configuración LoRA...")
    lora_config = LoraConfig(
        r=8,
        lora_alpha=16,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    # ------------------------------------------------------------
    # Procesamiento del Dataset
    # ------------------------------------------------------------
    print("📥 Cargando dataset...")
    raw_dataset = load_dataset("json", data_files=DATA_FILE, split="train")

    SYSTEM_PROMPT = "Eres un asistente educativo en español que responde de forma clara y precisa."

    def qa_to_text(example):
        q = str(example.get("question", ""))
        a = str(example.get("answer", ""))
        conv = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": q},
            {"role": "assistant", "content": a},
        ]
        text = tokenizer.apply_chat_template(conv, tokenize=False, add_generation_prompt=False)
        return {"text": text}

    text_dataset = raw_dataset.map(qa_to_text)

    def tokenize_fn(batch):
        out = tokenizer(batch["text"], truncation=True, max_length=MAX_LENGTH, padding="max_length")
        out["labels"] = out["input_ids"].copy()
        return out

    tokenized_dataset = text_dataset.map(
        tokenize_fn,
        batched=True,
        remove_columns=text_dataset.column_names,
    )

    # ------------------------------------------------------------
    # Configuración del Entrenamiento
    # ------------------------------------------------------------
    training_args = TrainingArguments(
        output_dir=OUTPUT_DIR,
        num_train_epochs=NUM_EPOCHS,
        per_device_train_batch_size=BATCH_SIZE,
        gradient_accumulation_steps=GRAD_ACCUM,
        learning_rate=LR,
        weight_decay=0.01,
        warmup_ratio=0.03,
        logging_steps=5,
        save_steps=50,
        save_total_limit=1,
        fp16=(device == "cuda"),
        report_to="none",
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
    )

    print("🚂 Empezando el entrenamiento...")
    trainer.train()

    # ------------------------------------------------------------
    # Guardado Final
    # ------------------------------------------------------------
    print(f"💾 Guardando en {OUTPUT_DIR}...")
    trainer.save_model(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)
    
    end_dt = datetime.now()
    print(f"✅ Finalizado. Duración: {end_dt - start_dt}")

if __name__ == "__main__":
    main()
