import confmat
import utils
import os
 
def quality_score(tp, tn, fp, fn):
    if (tp + tn + 10 * fp + fn) != 0:
        return (tp + tn)/(tp + tn + 10 * fp + fn)
    else:
        raise(ValueError)
 
def compute_quality_for_corpus(corpus_dir):
    prediction = utils.read_classification_from_file(os.path.join(corpus_dir, '!prediction.txt'))
    truth = utils.read_classification_from_file(os.path.join(corpus_dir, '!truth.txt'))
    matrix = confmat.BinaryConfusionMatrix()
    matrix.compute_from_dicts(truth, prediction)
    dic = matrix.as_dict()
    return quality_score(dic['tp'], dic['tn'], dic['fp'], dic['fn'])
