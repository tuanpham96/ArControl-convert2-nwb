# Example workflow

## Requirements 

- `conda`

All steps assume to be inside this `example_workflow` folder, unless indicated otherwise.

## Installation

### 1. Preprocessing environment

This step creates an environment to faciliate converting ArControl `.aconf` file to `smcat` outputs. 

```bash
conda env create -f arctl-utils-env.yaml
conda activate arcontrol-utils
npm install state-machine-cat
export PATH=$PATH:node_modules/.bin
```

### 2. NWB Conversion environment

Either in the same environment, or in a separate environment for NWB conversion (remember to `conda deactvate` if so), do:

```bash
pip install -U git+https://github.com/chenxinfeng4/ArControl-convert2-nwb
```

or to install locally after cloning the parent repository

```bash
# assume inside `example_workflow` folder
pip install -e .. 
```

## Data

Inside the `data` folder:

```
task
├── GNG_2021.aconf            # [in]  given from arcontrol (optional input for step 2)
├── GNG_2021.smcat            # [out] output from step 1 (optional input for step 2)
├── GNG_2021_clean.smcat      # [out] output from step 1
├── GNG_2021.json             # [out] output from step 1 (optional input for step 2)
├── GNG_2021.png              # [out] output from step 1
└── GNG_2021.svg              # [out] output from step 1

acquisition
├── 2022-0625-121053.txt      # [in]  given from experiment (required input for step 2)
└── 2022-0625-121053.nwb      # [out] final output from step 2
```

Credit: These are data from Simon Daste, Brown University. 

## Steps

### 1. Convert task `.aconf` file to `.smcat`, `.json` and `.png`

- Activate environment and change `PATH` to use node packages. Skip this if already done

```bash
conda activate arcontrol-utils
export PATH=$PATH:node_modules/.bin
```

- Then convert to JSON, SVG, PNG to use for later

```bash
# GNG_2021.aconf -> GNG_2021.smcat
python -m arcontrol2smcat data/task/GNG_2021.aconf

# clean emojis
cp data/task/GNG_2021.smcat data/task/GNG_2021_clean.smcat
python utils/remove_emoji.py data/task/GNG_2021_clean.smcat

# task/GNG_2021.smcat -> JSON, SVG, PNG
smcat -T json data/task/GNG_2021_clean.smcat -o data/task/GNG_2021.json
smcat -T svg -d left-right data/task/GNG_2021.smcat
smcat -T png -d left-right data/task/GNG_2021.smcat
```

### 2. Convert to `NWB`

Head to `demo_convert.ipynb` notebook

## TODOs

- [ ] Step 1 needs to be automated
- [ ] Address the `TODO`s in `convert_cli.py`
