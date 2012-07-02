# -*- encoding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth import models
from sistema.models import *
from clientes.models import *
from django.forms import TextInput, Textarea

class TelefonoInline(admin.TabularInline):
    model = Telefono
    extra = 1

class EmailInline(admin.TabularInline):
    model = Email
    extra = 1

class ClienteOptions(admin.ModelAdmin):
#	list_display = ('nombre','cliente','ciudad','estado')
    list_display = ('__unicode__', 'razon_social', 'ciudad')
    list_filter = ('ciudad',)
    list_display_links = ('__unicode__', 'razon_social',)
    search_fields = ('nombre', 'apellido', 'cliente_nro','cuit')
    fieldsets = (
		('Información General',
		       {'fields':(('titulo', 'nombre','apellido'),('razon_social', 'cuit','cliente_nro')    )}),
#		('Datos de Contacto',
#		       {'fields':(('telefono_fijo', 'telefono_celular'), 'email')}),
		('Ubicación', { 
			'classes': ['collapse', 'wide', 'extrapretty'],
		       'fields':(('direccion','altura'),('pais','provincia', 'ciudad'))
			}),
            	)

    inlines = [TelefonoInline,EmailInline]

class CostoInline(admin.TabularInline):
    model = Costo
    formfield_overrides = {
	models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':50})},
        models.DecimalField: {'widget': TextInput(attrs={'size':'8'})},
    }
    fieldsets = (							#aca se podria definir el orden de las columnas
		(None, {
			'fields':('tipo', 'recurso','cantidad','unidad','valor_unitario','total','observaciones')
			}),
	        )
    extra = 1

class ConjuntoCostoOptions(admin.ModelAdmin):
    list_display = ('obra','cliente', 'ciudad')
    list_filter = ('cliente__ciudad','obra__estado')
    list_display_links = ('cliente','obra',)
    search_fields = ('cliente__nombre','cliente__razon_social','costo__observaciones')
    fieldsets = (
		(('Datos de la Obra'),
               		{'fields':(('cliente', 'obra'),)}),
		#	{'description': ('hola'),}),
	        )
    inlines = [CostoInline]

    
    def ciudad(self, obj):
        return obj.obra.getCiudad()
    ciudad.short_description = 'Ciudad de la Obra'

    def upper_case_cliente(self, obj):
      return ("%s" % (obj.cliente)).upper()

class ObraInline(admin.StackedInline):
     model = Obra 
     extra = 1 
     classes = ('collapse closed',)
     #list_display = ('obra')
     fieldsets = (
	('Dimensiones',
		       {'fields':(('largo', 'ancho', 'superficie' ),)}),	
	('Estructura', 
		       {#'classes': ['collapse', 'wide', 'extrapretty'],
		        'fields':(('cubierta','hierro', 'canaletas'),)
			}),
	('Cerramiento', 
		       {#'classes': ['collapse', 'wide', 'extrapretty'],
		        'fields':(('chapa','perimetroChapa','altoChapa','superficieChapa'),
				  ('bloque','perimetroBloque','altoBloque','superficieBloque'))
			}),		
	('Cubierta', 
               {'fields':(('tipoChapa','anchoCubierta','largoCubierta','superficieCubierta'),) }),
        ('Varios', 
		       {'classes': ['collapse', 'wide', 'extrapretty'],
		       'fields':(('porton','fieltro','tipo_obra'),('observacion' ))}),	
        )

#     formfield_overrides = {
#         models.TextField: {'widget': RichTextEditorWidget},
#     }


class CobroInline(admin.TabularInline):
    model = Cobro
    classes = ('collapse closed',)
    formfield_overrides = {
	models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':80})},
    }

class ConjuntoObraOptions(admin.ModelAdmin):
	list_display = ('nombre','cliente','ciudad','estado','getDirectorObra')
        list_filter = ('ciudad','estado',)
        list_display_links = list_display
#        list_editable = ('estado',)
#        raw_id_fields = ('cliente',)
	fieldsets = (
	       ('Datos de la Obra',
			       {'fields':(('cliente', 'nombre'),('ciudad','estado','director_obra' ),)}),		
	)

	inlines = [ObraInline,CobroInline]

admin.site.register(ConjuntoObra,ConjuntoObraOptions)
admin.site.register(Cliente,ClienteOptions)
admin.site.register(ConjuntoCosto,ConjuntoCostoOptions)

