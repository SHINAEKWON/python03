class calculator:
    """
    This calculator does dotproduct, vector addition and
    substraction vector operations.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Dotproduct multilies corresponding elements
of the two vectors and returns the sum of the products."""
        result = [v1e * v2e for v1e, v2e in zip(V1, V2)]
        summed = sum(result)
        print("Dot product is:", summed)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Addvec adds corresponding elements from both
vectors and returns the list of sums"""
        result = [float(v1e + v2e) for v1e, v2e in zip(V1, V2)]
        print("Add Vector is :", result)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Addvec substracts corresponding elements from both
vectors and returns the list of substractions"""
        result = [float(v1e - v2e) for v1e, v2e in zip(V1, V2)]
        print("Sous Vector is:", result)
