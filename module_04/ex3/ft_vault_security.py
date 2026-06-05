#!/usr/bin/env python3


def secure_archive(
    file_name: str, action: str = "read", content: str = ""
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(file_name, "r") as file:
                data = file.read()
                return True, data
        elif action == "write":
            with open(file_name, "w") as file:
                file.write(content)
                return True, "Content successfully written to file"
        else:
            return False, "Invalid action."
    except (FileNotFoundError, PermissionError, OSError) as e:
        return False, str(e)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive(file_name="secret.txt", action="read"))
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive(file_name="/etc/passwd", action="read"))
    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive(file_name="ft_vault_security.py", action="read"))
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive(file_name="secret.txt", action="write", content="hello"))
