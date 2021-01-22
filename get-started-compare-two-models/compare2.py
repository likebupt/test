import argparse
from pathlib import Path

parser = argparse.ArgumentParser("compare2")
parser.add_argument("--model1", type=str, help="The first model to compare with")
parser.add_argument("--eval_result1", type=str, help="The evaluation result of first model")
parser.add_argument("--model2", type=str, help="The second model to compare")
parser.add_argument("--eval_result2", type=str, help="The evaluation result of second model")
parser.add_argument("--best_model", type=str, help="The better model among the two")
parser.add_argument("--best_result", type=str, help="The better model evalution result among the two")

args = parser.parse_args()

lines = [
    f'Model #1: {args.model1}',
    f'Evaluation #1: {args.eval_result1}',
    f'Model #2: {args.model2}',
    f'Evaluation #2: {args.eval_result2}',
    f'Best model path: {args.best_model}',
    f'Best result path: {args.best_result}',
]

for line in lines:
    print(line)

# Compare and get the best model and best evaluation result.
# Here we select the first one for demo
best_model = (Path(args.model1) / 'model').read_text()
best_result = (Path(args.eval_result1) / 'eval_result').read_text()

print('Best model', best_model)
print('Best result', best_result)

# Save best model and best result to output file
(Path(args.best_model) / 'model').write_text(best_model)
(Path(args.best_result) / 'best_result').write_text(best_result)