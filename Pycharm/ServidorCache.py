
class ServidorCache:
    """
    Clase del servidor caché donde se almacenan parte de series/películas.
    """

    def __init__(self, identifier, country, capacity):
        """Instancia un Servidor de Caché

        Parameters
        ----------
        identifier : int
            Valor que identifica un servidor.
        country : str
            País donde está el servidor.
        capacity : int
            Cantidad de memoria de almacenamiento disponible.
        """
        self.identifier = identifier
        self.country = country
        self.capacity = capacity

    def __hash__(self):
        """Genera el valor hash identificativo del servidor

        Returns
        -------
        int
            Valor hash
        """
        pass

    def __str__(self):
        """Genera una cadena descriptiva del objeto

        Returns
        -------
        str
            Cadena descriptiva
        """
        pass

    def __repr__(self):
        """Genera una cadena descriptiva del objeto en colecciones

        Returns
        -------
        str
            Cadena descriptiva
        """
        pass

    def rellena(self, videos):
        """Dada una colección de videos,
           seleccionar de cada uno cuanta cantidad (entre 0 y 1)
           se almacena en el servidor.
           Se ha de optimizar para que el tiempo de emisión
           sea el máximo posible.

        Parameters
        ----------
        videos : collection
            Colección de videos que se quieren almacenar en el servidor.
        """
        pass

    def disponible(self, video):
        """Obtiene la cantidad de vídeo disponible en el servidor.

        Parameters
        ----------
        video : Video object
            Vídeo del cual se quiere saber la disponibilidad

        Returns
        -------
        float
            Cantidad del vídeo disponible
        """
        pass

    def almacenados(self):
        """Material almacenado en el servidor

        Returns
        -------
        set
            Conjunto de tuplas (video, cantidad) de los videos ALMACENADOS en el servidor.
        """
        pass

    def tiempo_emision(self):
        """A partir de los datos almacenados
           devolver número de usuarios satisfechos
           siguiendo la fórmula:
           \\sum_{i}^{v} \\text{espectadores}_i*\\text{size}_i*\\text{cantidadAlmacenada}_i

        Returns
        -------
        number
            Tiempo de Emision
        """
        pass