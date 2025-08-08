

__all__ = ["send", "attach_file"]


def send(email: str, message: str) -> None:
    print(f'Sending "{message}" to {email}')


def attach_file(filename: str) -> None:
    print(f'Attach {filename} to the message')
