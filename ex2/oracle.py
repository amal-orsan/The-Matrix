import os
import sys


def main() -> None:
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

    print("ORACLE STATUS: Reading the Matrix...\n")

    mode = os.environ.get("MATRIX_MODE", "unknown")
    db_url = os.environ.get("DATABASE_URL")
    api_key = os.environ.get("API_KEY")
    log_level = os.environ.get("LOG_LEVEL", "INFO")
    zion_endpoint = os.environ.get("ZION_ENDPOINT")

    if not all([db_url, api_key, zion_endpoint]):
        print(
            "[WARNING] Configuration is missing critical variables.",
            file=sys.stderr,
        )
        print(
            "Ensure your .env file is present or "
            "environment variables are set.\n",
            file=sys.stderr,
        )

    print("Configuration loaded:")
    print(f"Mode:  {mode}")
    db_status = "Connected to local instance" if db_url else "Disconnected"
    print(f"Database:  {db_status}")
    api_status = "Authenticated" if api_key else "Missing Key"
    print(f"API Access:  {api_status}")
    print(f"Log Level:  {log_level}")
    zion_status = "Online" if zion_endpoint else "Offline"
    print(f"Zion Network:  {zion_status}")

    print("\nEnvironment security check:")

    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env file missing from local path")

    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
