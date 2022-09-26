#!/bin/env python

import plottery_wrapper as p

# bkg_plot_order_4LepMET = [ "WZ", "Other", "VH", "TTZ", "ZZ" ]
# legend_labels_4LepMET = [ "WZ", "Other", "VH", "TTZ", "ZZ" ]
# sig_plot_order_4LepMET = [ "VVV" ]
# sig_labels_4LepMET = [ "VVV" ]
# colors_4LepMET = [7013, 920, 4024, 4305, 4020]

p.dump_plot(
        fnames=[
            "outputs/ZZ.root",
            "outputs/TTZ.root",
            "outputs/Higgs.root",
            "outputs/WZ.root",
            "outputs/Other.root",
            "outputs/VVV.root",
            # "outputs/WWZ.root",
            # "outputs/WZZ.root",
            # "outputs/ZZZ.root",
            ],
        sig_fnames=[
            "outputs/WWZ_EFT_FT0_3p0.root",
            "outputs/WZZ_EFT_FT0_3p0.root",
            "outputs/ZZZ_EFT_FT0_3p0.root",
            ],
        # data_fname="outputs/data.root",
        legend_labels=[
            "ZZ",
            "t#bar{t}Z",
            "Higgs",
            "WZ",
            "Other",
            "WWZ",
            ],
        signal_labels=[
            "WWZ EFT",
            "WZZ EFT",
            "ZZZ EFT",
            ],
        usercolors=[
            4020,
            4305,
            4024,
            7013,
            920,
            ],
        filter_pattern="CutOffZST__STLepFit,CutOnZFJST__STLepHadFit,CutOnZNoFJST__STLepFit,CutEMuST__STLepFit",
        dogrep=True,
        extraoptions={
            "print_yield": True,
            "lumi_value": 59.8,
            "nbins": 20,
            "yaxis_log": True,
            "ratio_range": [0., 2.],
            # "signal_scale":"auto",
            "legend_scalex": 2.0,
            "legend_ncolumns": 3,
            },
        # _plotter=p.plot_cut_scan,
        )
