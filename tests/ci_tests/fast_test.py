from tests import basic_test
import torch

# Test with a few basic options
basic_test(backend='lightwood',use_gpu=torch.cuda.is_available(),ignore_columns=[], IS_CI_TEST=True)
print('\n\n=============[Success]==============\n     Finished running quick test !\n=============[Success]==============\n\n')
