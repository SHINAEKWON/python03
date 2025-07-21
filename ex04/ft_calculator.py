class calculator:
    """
    This calculator does dotproduct, vector addition and
    substraction vector operations.
    """
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        result = [v1e * v2e for v1e, v2e in zip(V1, V2)]
        summed = sum(result)
        print("Dot product is:", summed)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        result = [float(v1e + v2e) for v1e, v2e in zip(V1, V2)]
        print("Add Vector is :", result)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        result = [float(v1e - v2e) for v1e, v2e in zip(V1, V2)]
        print("Sous Vector is:", result)
