# Running the tutorial on your own laptop

Use this if you prefer your own machine to Google Colab. Please do it **before the session**: the download and installation take roughly 10 minutes and a few GB of disk space.

## What you need first

- **git**
- **conda**, from [Miniforge](https://conda-forge.org/download/) or Miniconda. On Windows, run the commands below in the "Miniforge Prompt" (or "Anaconda Prompt").

## Setup

Run these one at a time in a terminal.

```bash
git clone https://github.com/f-charton/Transformer-demo
```

```bash
cd Transformer-demo
```

```bash
conda env create -f environment.yml
```

```bash
conda activate env_axolver
```

```bash
jupyter notebook
```
Jupyter notebook opens in your browser. Open `Tutorial.ipynb`.

## Check which hardware you have

With the environment active, run:

```bash
python -c "import torch; print('NVIDIA GPU:', torch.cuda.is_available(), '| Apple GPU:', torch.backends.mps.is_available())"
```

## If something goes wrong

- **`ModuleNotFoundError: No module named 'train'`**: the notebook was moved out of the `notebooks` folder. It must stay there, because it looks for the code one folder up.
- **`conda activate` fails**: close and reopen the terminal, or run `conda init` once and reopen it.

## Later sessions

You only need the last two steps: `conda activate env_axolver`, then `jupyter lab` from the `Transformer-demo` folder.
