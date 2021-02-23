from experiments.mixed import MixedExperiment
from spn.structure.StatisticalTypes import MetaType


class Exp_parkinsons(MixedExperiment.MixedExperiment):

    # 23 attributes after filtering with 10 folds
    meta_types = [MetaType.REAL, MetaType.REAL, MetaType.REAL, MetaType.REAL, MetaType.REAL,
                  MetaType.REAL, MetaType.REAL, MetaType.REAL, MetaType.REAL, MetaType.REAL,
                  MetaType.REAL, MetaType.REAL, MetaType.REAL, MetaType.REAL, MetaType.REAL,
                  MetaType.REAL, MetaType.DISCRETE, MetaType.REAL, MetaType.REAL, MetaType.REAL,
                  MetaType.REAL, MetaType.REAL, MetaType.REAL]
    var_types_string = "ccccccccccccccccucccccc"

    def run(self, run: int, n_folds: int, fold_log: bool):
        print("\n------------------------------------------------------------------")
        print("------------------------------------------------------------------")
        print("---------------------------- PARKINSONS --------------------------")
        print("------------------------------------------------------------------")
        print("------------------------------------------------------------------\n")

        super().run(run, n_folds, fold_log)


def main():
    run = 1
    n_folds = 10

    data_name = "parkinsons"
    fold_log = True
    exp = Exp_parkinsons(data_name)
    exp.run(run, n_folds, fold_log)


if __name__ == "__main__":
    main()

