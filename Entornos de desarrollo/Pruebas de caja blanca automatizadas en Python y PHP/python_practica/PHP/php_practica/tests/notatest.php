<?php
use PHPUnit\Framework\TestCase;

require_once __DIR__ . '/../src/Nota.php';

class NotaTest extends TestCase
{
	public function testNotaNegativa()
	{
		$this->assertEquals("Nota no válida", evaluarNota(-1));
	}

	public function testNotaMayorQueDiez()
	{
		$this->assertEquals("Nota no válida", evaluarNota(11));
	}

	public function testSobresaliente()
	{
		$this->assertEquals("Sobresaliente", evaluarNota(9));
	}

	public function testNotable()
	{
		$this->assertEquals("Notable", evaluarNota(7));
	}

	public function testAprobado()
	{
		$this->assertEquals("Aprobado", evaluarNota(5));
	}

	public function testSuspenso()
	{
		$this->assertEquals("Suspenso", evaluarNota(3));
	}

	public function testSuspensoPorDebajoDeTres()
	{
		$this->assertEquals("Suspenso", evaluarNota(2));
	}

	public function testMensajeExtra()
	{
		$this->assertEquals("Función no ejecutada", mensajeExtra());
	}
}
