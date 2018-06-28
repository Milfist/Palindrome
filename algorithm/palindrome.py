class Palindrome:

    """
        Recorremos la mitad de la cadena comparando cada elemento con su opuesto.
        Esto nos daría una complejidad de O(n/2).
        No tiene en cuenta mayusculas, espacios, etc. eso es solo transformar la cadena
        pero añade más complegidad y depende un poco de la intrepretación de cada uno si
        Oso == oso.

    """
    @staticmethod
    def is_palindrome(chain):
        for i in range(len(chain) // 2):
            if chain[i] != chain[-1 - i]:
                return False
        return True
