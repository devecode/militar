from django.db import models


class Cartilla(models.Model):
    CAS='CASADO'
    SOL='SOLTERO'
    ESTADO_CIVIL=[
        (CAS,'CASADO'),
        (SOL,'SOLTERO')
    ]
    SI='SI'
    NO='NO'
    LEER_ESCRIBIR=[
        (SI,'SI'),
        (NO,'NO')
    ]
    clase = models.IntegerField('CLASE', default=0)
    nombre = models.CharField('NOMBRE', max_length=500)
    fecha_nacimiento = models.DateField('FECHA DE NACIMIENTO')
    nacio = models.CharField('NACIÓ EN', max_length=400)
    papa = models.CharField('HIJO DE', max_length=500)
    mama = models.CharField('Y DE', max_length=500)
    estado = models.CharField('ESTADO CIVIL', 
        max_length=10,
        choices=ESTADO_CIVIL,
        default=SOL
    )
    ocupacion = models.CharField('OCUPACIÓN', max_length=200)
    leer_escribir = models.CharField('¿SABE LEER Y ESCRIBIR?', 
        max_length=10,
        choices=LEER_ESCRIBIR,
        default=SI
    )
    curp = models.CharField('CURP', max_length=500)
    grado_maximo =  models.CharField('GRADO MÁXIMO DE ESTUDIOS', max_length=500)
    domicilio = models.CharField('DOMICILIO', max_length=500)
    presidente = models.CharField('PRESIDENTE', max_length=500)
    lugar = models.CharField('LUGAR', max_length=500)
    fecha = models.DateField('FECHA', auto_now_add=True)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.curp)

    def save(self):
        self.nombre = self.nombre.upper()
        self.curp = self.curp.upper()
        super(Cartilla, self).save()
    
    class Meta:
        verbose_name_plural = 'Cartillas'