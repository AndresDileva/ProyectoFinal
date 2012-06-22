# -*- encoding: utf-8 -*-
from django.db import models
from sistema.models import *
from clientes.models import *
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.

class Presupuesto(models.Model):       
	cliente = models.ForeignKey(Cliente)
	obra = ChainedForeignKey(
		ConjuntoObra, 
		chained_field="cliente",
		chained_model_field="cliente", 
		show_all=False, 
		auto_choose=True
    	)
    	tareas = models.DecimalField('Tareas preliminares',default = 0.0,max_digits = 7, decimal_places = 2)
    	suelo = models.DecimalField('Movimiento de Suelo',default = 0.0, max_digits = 7, decimal_places = 2)
   	#Estructura Hormigon
    	bases = models.DecimalField('Bases',default = 0.0, max_digits = 7, decimal_places = 2)
    	vigas_fundacion = models.DecimalField('Vigas fundación',default = 0.0, max_digits = 7, decimal_places = 2)
    	columnas = models.DecimalField('Columnas',default = 0.0, max_digits = 7, decimal_places = 2)
    	vigas_encadenado = models.DecimalField('Vigas encadenado',default = 0.0, max_digits = 7, decimal_places = 2)
    	piso = models.DecimalField('Piso',default = 0.0, max_digits = 7, decimal_places = 2)
    	#Estructura Metalica
    	platinas = models.DecimalField('Platinas',default = 0.0, max_digits = 7, decimal_places = 2)
    	columnas_principales = models.DecimalField('Columnas Principales',default = 0.0, max_digits = 7, decimal_places = 2)
    	columnas_mojinete = models.DecimalField('Columnas Mojinete',default = 0.0, max_digits = 7, decimal_places = 2)
    	arcos_vigas = models.DecimalField('Arcos/Vigas',default = 0.0, max_digits = 7, decimal_places = 2)
    	buloneria = models.DecimalField('Bulonería',default = 0.0, max_digits = 7, decimal_places = 2) 
    	tensores = models.DecimalField('Tensores',default = 0.0, max_digits = 7, decimal_places = 2)   
    	metalica_otros  = models.DecimalField('Otros',default = 0.0, max_digits = 7, decimal_places = 2)
    	#Cubierta Metalica
    	correas = models.DecimalField('Correas',default = 0.0, max_digits = 7, decimal_places = 2)
    	fieltro_aislante = models.DecimalField('Fieltro Aislante',default = 0.0, max_digits = 7, decimal_places = 2)
    	chapa = models.DecimalField('Chapa',default = 0.0, max_digits = 7, decimal_places = 2)
    	canaletas = models.DecimalField('Canaletas',default = 0.0, max_digits = 7, decimal_places = 2)
    	zingueria = models.DecimalField('Zinguería',default = 0.0, max_digits = 7, decimal_places = 2)
    	cubierta_otros = models.DecimalField('Otros',default = 0.0, max_digits = 7, decimal_places = 2)
    	#Varios
    	contrapisos = models.DecimalField('Contrapisos',default = 0.0, max_digits = 7, decimal_places = 2)
    	carpetas = models.DecimalField('Carpetas',default = 0.0, max_digits = 7, decimal_places = 2)
    	revoques = models.DecimalField('Revoques',default = 0.0, max_digits = 7, decimal_places = 2)
    	herreria = models.DecimalField('Herrería',default = 0.0, max_digits = 7, decimal_places = 2)
    	pisos_revestimientos = models.DecimalField('Pisos/Revestimientos',default = 0.0, max_digits = 7, decimal_places = 2)
    	cielorrasos = models.DecimalField('Cielorrasos',default = 0.0, max_digits = 7, decimal_places = 2)
    	carpinteria = models.DecimalField('Carpintería',default = 0.0, max_digits = 7, decimal_places = 2)
    	pintura = models.DecimalField('Pintura',default = 0.0, max_digits = 7, decimal_places = 2)
    	limpieza_obra = models.DecimalField('Limpieza de Obra',default = 0.0, max_digits = 7, decimal_places = 2)

    	#Entrepiso
    	hormigon = models.DecimalField('Hormigón',default = 0.0, max_digits = 7, decimal_places = 2)
    	metalico = models.DecimalField('Metalico',default = 0.0, max_digits = 7, decimal_places = 2)
    	#Instalaciones
    	sanitaria = models.DecimalField('Sanitaria',default = 0.0, max_digits = 7, decimal_places = 2)
    	gas = models.DecimalField('Gas',default = 0.0, max_digits = 7, decimal_places = 2)
    	agua = models.DecimalField('Agua',default = 0.0, max_digits = 7, decimal_places = 2)
    	pluviales = models.DecimalField('Pluvial',default = 0.0, max_digits = 7, decimal_places = 2)
    	electrica = models.DecimalField('Eléctrica',default = 0.0, max_digits = 7, decimal_places = 2)
    	aire_calefaccion = models.DecimalField('AA / Calefacción',default = 0.0, max_digits = 7, decimal_places = 2)
    	instalaciones_otros = models.DecimalField('Otros',default = 0.0, max_digits = 7, decimal_places = 2)
	#Cerramiento Mamposteria
    	mamposteria = models.DecimalField('Mampostería',default = 0.0, max_digits = 7, decimal_places = 2)
    	correas_cerramiento = models.DecimalField('Correas',default = 0.0, max_digits = 7, decimal_places = 2)
    	fieltro_aislante_cerramiento = models.DecimalField('Fieltro Aislante',default = 0.0, max_digits = 7, decimal_places = 2)
    	chapa_cerramiento = models.DecimalField('Chapa',default = 0.0, max_digits = 7, decimal_places = 2)
    	buloneria_cerramiento = models.DecimalField('Bulonería',default = 0.0, max_digits = 7, decimal_places = 2)
    	zingueria_cerramiento = models.DecimalField('Zinguería',default = 0.0, max_digits = 7, decimal_places = 2)
    	otros_cerramiento = models.DecimalField('Otros',default = 0.0, max_digits = 7, decimal_places = 2)

	# Generales de la obra
    	monto_obra = models.DecimalField('Monto Total',default = 0.0, max_digits = 12, decimal_places = 2)
    	monto_general = models.DecimalField('Monto General',default = 0.0, max_digits = 12, decimal_places = 2)
    	monto_estructura_hormigon = models.DecimalField('Monto Est. Ho.',default = 0.0, max_digits = 12, decimal_places = 2)
    	monto_estructura_metalica = models.DecimalField('Monto Est. Metal.',default = 0.0, max_digits = 12, decimal_places = 2)
    	monto_cerramiento = models.DecimalField('Monto Cerramiento',default = 0.0, max_digits = 12, decimal_places = 2)
    	monto_cubierta_metalica = models.DecimalField('Monto Cubierta',default = 0.0, max_digits = 12, decimal_places = 2)
    	monto_instalaciones = models.DecimalField('Monto Instalaciones',default = 0.0, max_digits = 12, decimal_places = 2)
    	monto_varios = models.DecimalField('Monto Varios',default = 0.0, max_digits = 12, decimal_places = 2)


	class Meta:
		verbose_name = 'Presupuesto'        
		verbose_name_plural = "Administrar Presupuestos"

        @property
	def suma_st(self):
		self.monto_obra = '100'
	    	self.monto_general = "100"
	    	self.monto_estructura_hormigon =  100
	    	self.monto_estructura_metalica =  100
	    	self.monto_cerramiento =  100
	    	self.monto_cubierta_metalica =  100
	    	self.monto_instalaciones =  100
	    	self.monto_varios =  100
		return self.suma_st() 

	def suma_monto_obra(self):
		#self.monto_obra = (self.monto_general * self.monto_estructura_hormigon)
		return self.monto_obra 

   	def save(self):
        	self.monto_obra = self.suma_monto_obra()
        	super(Presupuesto, self).save() 


	def __unicode__(self):
	        return u'%s (%s)' % (self.cliente, self.obra)



class Suma(models.Model):
    quantity = models.IntegerField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tot = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total(self):
        return self.quantity * self.price

    def __unicode__(self):
	return '%s' % (self.quantity * self.price)
