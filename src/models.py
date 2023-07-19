import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    contraseña = Column(String(250), nullable=False)
    fechasuscripcion = Column(String(250), nullable=False)
    favorito_personaje = Column(Integer, ForeignKey('favoritos_personajes.id.personaje'), nullable=False)
    favorito_vehiculo = Column(Integer, ForeignKey('favoritos_vehiculos.id_vehiculo'), nullable=False)
    favorito_planeta = Column(Integer, ForeignKey('favoritos_planetas.id_planeta'), nullable=False)
    
    


class Planeta(Base):
    __tablename__ = 'planeta'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    poblacion = Column(String(250))
    tamaño = Column(String(250), nullable=False)
    gravedad = Column(String(250), nullable=False)
    terreno = Column(String(250), nullable=False)
    favoritos_planetas = relationship('FavoritoPlaneta', backref='planeta', lazy=True)


class Personaje(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    altura = Column(String(250))
    nacimiento = Column(String(250), nullable=False)
    genero = Column(String(250), nullable=False)
    colorojos = Column(String(250), nullable=False)
    colorpelo = Column(String(250), nullable=False)
    peso = Column(String(250), nullable=False)
    favoritos_personajes = relationship('FavoritoPersonaje', backref='personaje', lazy=True)


class Vehiculo(Base):
    __tablename__ = 'vehiculos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    modelo = Column(String(250))
    clase = Column(String(250), nullable=False)
    coste = Column(String(250), nullable=False)
    capacidad = Column(String(250), nullable=False)
    tamaño = Column(String(250), nullable=False)
    favorito_vehiculo = relationship('FavoritoVehiculo', backref='vehiculo', lazy=True)
    

class FavoritoPlaneta(Base):
    __tablename__ = 'favoritos_planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    id_planeta = Column(Integer, ForeignKey('planeta.id'), nullable=False)
    favorito_planeta_personaje = relationship('Usuario', backref='favoritos_planetas', lazy=True)
    



class FavoritoPersonaje(Base):
    __tablename__ = 'favoritos_personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    id_personaje = Column(Integer, ForeignKey('personajes.id'), nullable=False)
    favorito_planeta_personaje = relationship('Usuario', backref='favoritos_personajes', lazy=True)

class FavoritoVehiculo(Base):
    __tablename__ = 'favoritos_vehiculos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    id_vehiculo = Column(Integer, ForeignKey('vehiculos.id'), nullable=False)   
    favorito_planeta_vehiculo = relationship('Usuario', backref='favoritos_vehiculos', lazy=True)
    


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
