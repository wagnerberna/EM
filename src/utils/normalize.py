from unicodedata import normalize


class NormalizeFields:
    def string(self, field):
        normalize_field = field.lower().strip()
        normalize_field = (
            normalize("NFKD", normalize_field).encode("ASCII", "ignore").decode("utf-8")
        )
        return normalize_field

    def cpf(self, cpf):
        normalize_cpf = cpf.strip().replace("-", "").replace(".", "")
        return normalize_cpf
