from flask_marshmallow import Marshmallow

ma = Marshmallow()

#Esquema de usuario
class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('id', 'usuario', 'clave')

#Esquema de película
class PelículaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'estreno', 'director', 'reparto', 'genero', 'sinopsis')


pelicula_schema = PelículaSchema()
peliculas_schema = PelículaSchema(many=True)