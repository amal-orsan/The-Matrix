import importlib
import sys


REQUIRED: dict[str, str] = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
}


def check_dependencies() -> dict[str, str]:
    status: dict[str, str] = {}
    missing = False

    print("Checking dependencies:")
    for lib, desc in REQUIRED.items():
        try:
            mod = importlib.import_module(lib)
            version = getattr(mod, "__version__", "unknown")
            print(f"[OK] {lib} ({version}) - {desc}")
            status[lib] = version
        except ImportError:
            print(f"[MISSING] {lib} - Required package is absent")
            missing = True

    try:
        import requests
        print(f"[OK] requests ({requests.__version__}) - Network access ready")
        status["requests"] = requests.__version__
    except ImportError:
        pass

    if missing:
        print("\nError: Missing required core dependencies.", file=sys.stderr)
        print(
            "To resolve using pip, run: pip install -r requirements.txt",
            file=sys.stderr,
        )
        print("To resolve using Poetry, run: poetry install", file=sys.stderr)
        sys.exit(1)

    return status


def analyze_matrix_data() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    rng = np.random.default_rng(seed=42)
    signal = rng.normal(loc=0.0, scale=1.0, size=1000)

    dataframe = pd.DataFrame({"signal": signal})
    summary = dataframe["signal"].describe()

    print("Statistical summary:")
    print(f"  mean: {summary['mean']:.4f}")
    print(f"  std:  {summary['std']:.4f}")
    print(f"  min:  {summary['min']:.4f}")
    print(f"  max:  {summary['max']:.4f}")

    print("Generating visualization...")
    fig, axis = plt.subplots()
    axis.hist(dataframe["signal"], bins=30)
    axis.set_title("Matrix Data Distribution")
    axis.set_xlabel("Signal")
    axis.set_ylabel("Frequency")
    fig.savefig("matrix_analysis.png")
    plt.close(fig)

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def compare_pip_poetry(versions: dict[str, str]) -> None:
    print("\nDependency management comparison:")
    print("pip:")
    print("  - Reads requirements.txt")
    print("  - Does not manage virtual environments on its own")
    print("  - No built-in lock file (pip freeze must be run manually)")
    print("  - Install with: pip install -r requirements.txt")
    print("Poetry:")
    print("  - Reads pyproject.toml")
    print("  - Creates and manages its own virtual environment")
    print("  - Generates poetry.lock for reproducible installs")
    print("  - Install with: poetry install")

    print("\nInstalled package versions:")
    for lib, version in versions.items():
        print(f"  {lib}: {version}")


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    versions = check_dependencies()
    analyze_matrix_data()
    compare_pip_poetry(versions)


if __name__ == "__main__":
    main()
