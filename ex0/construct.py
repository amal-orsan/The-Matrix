import os
import sys
import site


def is_virtual_environment() -> bool:
    return sys.prefix != sys.base_prefix


def print_outside_matrix() -> None:
    print("MATRIX STATUS: You're still plugged in\n")
    print(f"Current Python:  {sys.executable}")
    print("Virtual Environment:  None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print(r"matrix_env\Scripts\activate  # On Windows")
    print("\nThen run this program again.")


def print_inside_construct() -> None:
    env_path = sys.prefix
    env_name = os.path.basename(env_path)

    if hasattr(site, "getsitepackages"):
        site_packages = site.getsitepackages()[0]
    else:
        site_packages = "Unknown"

    print("\nMATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python:  {sys.executable}")
    print(f"Virtual Environment:  {env_name}")
    print(f"Environment Path:  {env_path}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")
    print("Package installation path:")
    print(f"{site_packages}\n")


def main() -> None:
    if not is_virtual_environment():
        print_outside_matrix()
    else:
        print_inside_construct()


if __name__ == "__main__":
    main()
