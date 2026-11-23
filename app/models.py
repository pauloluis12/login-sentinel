from dataclasses import dataclass
from datetime import datetime


@dataclass
class LoginEvent:
    """Uma tentativa de login: quem tentou, de onde, quando e se deu certo."""

    username: str        # nome de usuário digitado
    ip: str              # endereço de onde veio a tentativa
    success: bool        # True = entrou, False = errou a senha
    timestamp: datetime  # data e hora da tentativa

    def is_failure(self) -> bool:
        """Retorna True quando a tentativa falhou."""
        return not self.success