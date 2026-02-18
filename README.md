# 🇧🇬 Bulgarian Name Generator

A trigram-based statistical model that generates authentic Bulgarian names using character-level Markov chains trained on real name data.

## How It Works

The model learns the probability of each character following any two-character sequence (trigram) from a dataset of Bulgarian names. During generation, it samples from these learned distributions to produce new, realistic-sounding names — separately for male and female names.

**Training** (`model_training.py`) reads the CSV dataset, builds two trigram probability matrices (one per gender), and saves them as `.npy` files.

**Generation** (`main.py`) loads the matrices and samples character-by-character until it hits an end-of-sequence token or the name length limit.

## Setup

**Requirements:** Python 3, `numpy`, `pandas`

```bash
pip install numpy pandas
```

**Train the model** (run once to generate the `.npy` matrix files):

```bash
python model_training.py
```

**Generate names:**

```bash
python main.py
```

You'll be prompted to choose a gender (`M` or `F`), and 10 names will be generated.

## Dataset

The model expects a `names_dataset.csv` file with two columns:

| Column   | Description                  |
|----------|------------------------------|
| `name`   | Bulgarian name in Cyrillic   |
| `gender` | `M` for male, `F` for female |

## Example Output

```
Gender of for name generation (M/F): M
Иван
Георги
Милен
Красимир
...
```

## Project Structure

```
├── main.py              # Name generation script
├── model_training.py    # Trigram model training
├── names_dataset.csv    # Training data
├── trigram_male.npy     # Trained male model (generated)
└── trigram_female.npy   # Trained female model (generated)
```

## Notes

- The Bulgarian alphabet used contains 30 Cyrillic characters plus a special end-of-sequence token (`.`)
- Names are capped at 20 characters to prevent degenerate outputs
- The model is entirely statistical — no neural networks involved
