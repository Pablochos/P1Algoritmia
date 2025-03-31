
class ServidorMaestro:
    """
    Servidor central que gestiona las conexiones entre servidores cache
    """

    def __init__(self, servidores, distancias):
        """Instancia el servidor central

        Parameters
        ----------
        servidores : Iterable
            Conjunto de servidores cache disponibles
        distancias : dict{ServidorCache: dict{ServidorCache: int}}
            Grafo de distancias en milisegundos entre servidores.
        """
        self.servidores = set(servidores)
        self.distancias = distancias

    def get_grafo(self):
        """Devuelve el grafo de distancias recibido

        Returns
        -------
        dict{ServidorCache: dict{ServidorCache: int}}
            Grafo de distancias en milisegundos entre servidores.
        """
        pass

    def get_grafo_simplificado(self):
        """Devuelve el grafo de distancias simplificado

        Returns
        -------
        dict{ServidorCache: dict{ServidorCache: int}}
            Grafo de distancias en milisegundos entre servidores.
        """
        pass

    def simplifica_grafo(self):
        """A partir del grafo de distancias
           hacer una simplificación de la estrucutra
           de datos para ahorrar espacio y tiempo.
        """
        pass

    def mas_cercano(self, servidor):
        """Reporta el servidor más cercano al dado por parámetro

        Parameters
        ----------
        servidor : ServidorCache

        Returns
        -------
        ServidorCache
            Servidor más cercano
        """
        pass