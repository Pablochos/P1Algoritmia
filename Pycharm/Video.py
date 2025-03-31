
class Video:
    """
    Clase Video.
    Representa una serie o película.
    """

    def __init__(self, name, size, fee):
        """Crea un objeto de clase Video

        Parameters
        ----------
        name : str
            Nombre de la serie/película
        size : number
            Tamaño en memoria de la serie/película
        fee : number
            Coste de visualización de la serie/película
        """
        self.name = name
        self.size = size
        self.fee = fee

    def __hash__(self):
        """Genera el valor hash identificativo del vídeo

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
        """Genera una cadena descriptiva del objeto dentro de colecciones

        Returns
        -------
        str
            Cadena descriptiva
        """
        pass

    def set_users(self, country, users):
        """Dado un pais y un número de usuarios
           almacena para este vídeo la cantidad de espectadores que tiene.

        Parameters
        ----------
        country : str
            País desde donde se ve la serie/película
        users : int
            Número de espectadores
        """
        pass

    def get_users(self, country):
        """Dado un país, obtiene el número de usuarios.

        Parameters
        ----------
        country : str
            País desde donde se ve la serie/película

        Returns
        -------
        int
            Número de espectadores para el país `country`
        """
        pass