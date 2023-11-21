# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:08:45 2023

@author: Irfan Ali 
"""


import os
import sys
import logging
import random
import time
import shutil
import numpy as np
from collections import Counter
from tqdm import tqdm
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from RearEndUtils import analysisUtils as analysis
from RearEndUtils import fileUtils as procFile


def getArranged(ddata):
    models = []
    for itr, myDict in enumerate(ddata):
        temp = myDict["file"].split("_")
        models.append(temp[-2])
    counts = Counter(models)
    count_list = [[char, count] for char, count in counts.items()]
    count_list.sort(key=lambda x: x[1], reverse=True)
    result = [[char, count] for char, count in count_list if count >= 5]

    return result


def plotRegression(x, y):
    regres = LinearRegression()
    imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
    y_imputed = imputer.fit_transform(np.array(y).reshape(-1, 1))
    regres.fit(np.array(x).reshape(-1, 1), y_imputed)
    m = regres.coef_.flatten()[-1]
    c = regres.intercept_.flatten()[-1]
    return m, c


def plotData(
    ddata,
    name,
    regres=True,
    lim=True,
    pltType="scatter",
    regColor="red",
    limColor="black",
):
    year = []
    gsi_1 = []
    hic_1 = []
    prob_head_1 = []
    hic36_1 = []
    prob_head36_1 = []
    hic15_1 = []
    prob_head15_1 = []
    ms3h_1 = []
    ms3_1 = []
    cti_1 = []
    csi_1 = []
    f_val_1 = []
    f_prob_1 = []
    f_flag_1 = []
    nfa_1 = []
    nea_1 = []
    nfp_1 = []
    nep_1 = []
    nkmm_1 = []

    gsi_2 = []
    hic_2 = []
    prob_head_2 = []
    hic36_2 = []
    prob_head36_2 = []
    hic15_2 = []
    prob_head15_2 = []
    ms3h_2 = []
    ms3_2 = []
    cti_2 = []
    csi_2 = []
    f_val_2 = []
    f_prob_2 = []
    f_flag_2 = []
    nfa_2 = []
    nea_2 = []
    nfp_2 = []
    nep_2 = []
    nkmm_2 = []

    os.makedirs(os.path.join(base_path, "Results", name))

    if pltType == "scatter":
        colors = [
            f"#{random.randint(0, 255):02X}{random.randint(0, 255):02X}{random.randint(0, 255):02X}"
            for _ in data
        ]

        for itr, myDict in enumerate(ddata):
            year.append(int(myDict["date"]["year"]))
            gsi_1.append(myDict["proc_01"]["gsi"])
            hic_1.append(myDict["proc_01"]["hic"])
            prob_head_1.append(myDict["proc_01"]["prob_head"])
            hic36_1.append(myDict["proc_01"]["hic36"])
            prob_head36_1.append(myDict["proc_01"]["prob_head36"])
            hic15_1.append(myDict["proc_01"]["hic15"])
            prob_head15_1.append(myDict["proc_01"]["prob_head15"])
            ms3h_1.append(myDict["proc_01"]["ms3h"])
            ms3_1.append(myDict["proc_01"]["ms3"])
            cti_1.append(myDict["proc_01"]["cti"])
            csi_1.append(myDict["proc_01"]["csi"])
            f_val_1.append(myDict["proc_01"]["fval"])
            f_prob_1.append(myDict["proc_01"]["f_prob"])
            f_flag_1.append(myDict["proc_01"]["f_flag"])
            nfa_1.append(myDict["proc_01"]["nfa"])
            nea_1.append(myDict["proc_01"]["nea"])
            nfp_1.append(myDict["proc_01"]["nfp"])
            nep_1.append(myDict["proc_01"]["nep"])
            try:
                nkmm_1.append(
                    max(
                        [
                            myDict["proc_01"]["nfa"],
                            myDict["proc_01"]["nea"],
                            myDict["proc_01"]["nfp"],
                            myDict["proc_01"]["nep"],
                        ]
                    )
                )
            except:
                nkmm_1.append(None)

            gsi_2.append(myDict["proc_02"]["gsi"])
            hic_2.append(myDict["proc_02"]["hic"])
            prob_head_2.append(myDict["proc_02"]["prob_head"])
            hic36_2.append(myDict["proc_02"]["hic36"])
            prob_head36_2.append(myDict["proc_02"]["prob_head36"])
            hic15_2.append(myDict["proc_02"]["hic15"])
            prob_head15_2.append(myDict["proc_02"]["prob_head15"])
            ms3h_2.append(myDict["proc_02"]["ms3h"])
            ms3_2.append(myDict["proc_02"]["ms3"])
            cti_2.append(myDict["proc_02"]["cti"])
            csi_2.append(myDict["proc_02"]["csi"])
            f_val_2.append(myDict["proc_02"]["fval"])
            f_prob_2.append(myDict["proc_02"]["f_prob"])
            f_flag_2.append(myDict["proc_02"]["f_flag"])
            nfa_2.append(myDict["proc_02"]["nfa"])
            nea_2.append(myDict["proc_02"]["nea"])
            nfp_2.append(myDict["proc_02"]["nfp"])
            nep_2.append(myDict["proc_02"]["nep"])
            try:
                nkmm_2.append(
                    max(
                        [
                            myDict["proc_02"]["nfa"],
                            myDict["proc_02"]["nea"],
                            myDict["proc_02"]["nfp"],
                            myDict["proc_02"]["nep"],
                        ]
                    )
                )
            except:
                nkmm_2.append(None)

        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        ax1.scatter(year, gsi_1, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, gsi_1)
            ax1.plot(np.array(year), m * np.array(year) + c, color=regColor)
        ax1.set_ylabel("GSI (Right Front Seat)")
        # ax1.grid(True)
        ax2.scatter(year, gsi_2, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, gsi_2)
            ax2.plot(np.array(year), m * np.array(year) + c, color=regColor)
        ax2.set_ylabel("GSI (Left Front Seat)")
        # ax2.grid(True)
        fig.suptitle(f"GSI ({name})")
        plt.xlabel("Year")
        fig.savefig(os.path.join("Results", name, str(time.time()) + ".png"))
        plt.close()

        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        ax1.scatter(year, hic_1, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, hic_1)
            ax1.plot(np.array(year), m * np.array(year) + c, color=regColor)
        ax1.set_ylabel("HIC (Right Front Seat)")
        # ax1.grid(True)
        ax2.scatter(year, hic_2, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, hic_2)
            ax2.plot(np.array(year), m * np.array(year) + c, color=regColor)
        ax2.set_ylabel("HIC (Left Front Seat)")
        # ax2.grid(True)
        fig.suptitle(f"HIC ({name})")
        plt.xlabel("Year")
        fig.savefig(os.path.join("Results", name, str(time.time()) + ".png"))
        plt.close()

        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        ax1.scatter(year, prob_head_1, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, prob_head_1)
            ax1.plot(np.array(year), m * np.array(year) + c, color=regColor)
        ax1.set_ylabel("" r"$\rho$ (Right Front Seat)")
        # ax1.grid(True)
        ax2.scatter(year, prob_head_2, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, prob_head_2)
            ax2.plot(np.array(year), m * np.array(year) + c, color=regColor)
        ax2.set_ylabel("" r"$\rho$ (Left Front Seat)")
        # ax2.grid(True)
        fig.suptitle(f"Head Fracture Probability ({name})")
        plt.xlabel("Year")
        fig.savefig(os.path.join("Results", name, str(time.time()) + ".png"))
        plt.close()
        
        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        ax1.scatter(year, hic36_1, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, hic36_1)
            ax1.plot(np.array(year), m * np.array(year) + c, color=regColor)
        if lim:
            ax1.axhline(1000, color=limColor, linestyle="--")
        ax1.set_ylabel("HIC36 (Right Front Seat)")
        # ax1.grid(True)
        ax2.scatter(year, hic36_2, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, hic36_2)
            ax2.plot(np.array(year), m * np.array(year) + c, color=regColor)
        if lim:
            ax2.axhline(1000, color=limColor, linestyle="--")
        ax2.set_ylabel("HIC36 (Left Front Seat)")
        # ax2.grid(True)
        fig.suptitle(f"HIC36 ({name})")
        plt.xlabel("Year")
        fig.savefig(os.path.join("Results", name, str(time.time()) + ".png"))
        plt.close()
        
        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        ax1.scatter(year, prob_head36_1, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, prob_head36_1)
            ax1.plot(np.array(year), m * np.array(year) + c, color=regColor)
        ax1.set_ylabel("" r"$\rho$ (Right Front Seat)")
        # ax1.grid(True)
        ax2.scatter(year, prob_head36_2, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, prob_head36_2)
            ax2.plot(np.array(year), m * np.array(year) + c, color=regColor)
        ax2.set_ylabel("" r"$\rho$ (Left Front Seat)")
        # ax2.grid(True)
        fig.suptitle(f"Head Fracture Probability (HIC36) ({name})")
        plt.xlabel("Year")
        fig.savefig(os.path.join("Results", name, str(time.time()) + ".png"))
        plt.close()
        
        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        ax1.scatter(year, hic15_1, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, hic15_1)
            ax1.plot(np.array(year), m * np.array(year) + c, color=regColor)
        if lim:
            ax1.axhline(700, color=limColor, linestyle="--")
        ax1.set_ylabel("HIC15 (Right Front Seat)")
        # ax1.grid(True)
        ax2.scatter(year, hic15_2, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, hic15_2)
            ax2.plot(np.array(year), m * np.array(year) + c, color=regColor)
        if lim:
            ax2.axhline(700, color=limColor, linestyle="--")
        ax2.set_ylabel("HIC15 (Left Front Seat)")
        # ax2.grid(True)
        fig.suptitle(f"HIC15 ({name})")
        plt.xlabel("Year")
        fig.savefig(os.path.join("Results", name, str(time.time()) + ".png"))
        plt.close()
        
        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        ax1.scatter(year, prob_head15_1, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, prob_head15_1)
            ax1.plot(np.array(year), m * np.array(year) + c, color=regColor)
        ax1.set_ylabel("" r"$\rho$ (Right Front Seat)")
        # ax1.grid(True)
        ax2.scatter(year, prob_head15_2, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, prob_head15_2)
            ax2.plot(np.array(year), m * np.array(year) + c, color=regColor)
        ax2.set_ylabel("" r"$\rho$ (Left Front Seat)")
        # ax2.grid(True)
        fig.suptitle(f"Head Fracture Probability (HIC15) ({name})")
        plt.xlabel("Year")
        fig.savefig(os.path.join("Results", name, str(time.time()) + ".png"))
        plt.close()
        
        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        ax1.scatter(year, ms3h_1, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, ms3h_1)
            ax1.plot(np.array(year), m * np.array(year) + c, color=regColor)
        if lim:
            ax1.axhline(80, color=limColor, linestyle="--")
        ax1.set_ylabel("3ms (Right Front Seat)")
        # ax1.grid(True)
        ax2.scatter(year, ms3h_2, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, ms3h_2)
            ax2.plot(np.array(year), m * np.array(year) + c, color=regColor)
        if lim:
            ax2.axhline(80, color=limColor, linestyle="--")
        ax2.set_ylabel("3ms (Left Front Seat)")
        # ax2.grid(True)
        fig.suptitle(f"3ms (Head) Criterion ({name})")
        plt.xlabel("Year")
        fig.savefig(os.path.join("Results", name, str(time.time()) + ".png"))
        plt.close()

        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        ax1.scatter(year, ms3_1, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, ms3_1)
            ax1.plot(np.array(year), m * np.array(year) + c, color=regColor)
        if lim:
            ax1.axhline(60, color=limColor, linestyle="--")
        ax1.set_ylabel("3ms (Right Front Seat)")
        # ax1.grid(True)
        ax2.scatter(year, ms3_2, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, ms3_2)
            ax2.plot(np.array(year), m * np.array(year) + c, color=regColor)
        if lim:
            ax2.axhline(60, color=limColor, linestyle="--")
        ax2.set_ylabel("3ms (Left Front Seat)")
        # ax2.grid(True)
        fig.suptitle(f"3ms (Chest) Criterion ({name})")
        plt.xlabel("Year")
        fig.savefig(os.path.join("Results", name, str(time.time()) + ".png"))
        plt.close()

        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        ax1.scatter(year, cti_1, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, cti_1)
            ax1.plot(np.array(year), m * np.array(year) + c, color=regColor)
        ax1.set_ylabel("CTI (Right Front Seat)")
        # ax1.grid(True)
        ax2.scatter(year, cti_2, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, cti_2)
            ax2.plot(np.array(year), m * np.array(year) + c, color=regColor)
        ax2.set_ylabel("CTI (Left Front Seat)")
        # ax2.grid(True)
        fig.suptitle(f"CTI ({name})")
        plt.xlabel("Year")
        fig.savefig(os.path.join("Results", name, str(time.time()) + ".png"))
        plt.close()

        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        ax1.scatter(year, csi_1, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, csi_1)
            ax1.plot(np.array(year), m * np.array(year) + c, color=regColor)
        ax1.set_ylabel("CSI (Right Front Seat)")
        # ax1.grid(True)
        ax2.scatter(year, csi_2, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, csi_2)
            ax2.plot(np.array(year), m * np.array(year) + c, color=regColor)
        ax2.set_ylabel("CSI (Left Front Seat)")
        # ax2.grid(True)
        fig.suptitle(f"CSI ({name})")
        plt.xlabel("Year")
        fig.savefig(os.path.join("Results", name, str(time.time()) + ".png"))
        plt.close()

        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        ax1.scatter(year, f_val_1, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, f_val_1)
            ax1.plot(np.array(year), m * np.array(year) + c, color=regColor)
        ax1.set_ylabel("Femur Load (Right Front Seat)")
        # ax1.grid(True)
        ax2.scatter(year, f_val_2, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, f_val_2)
            ax2.plot(np.array(year), m * np.array(year) + c, color=regColor)
        ax2.set_ylabel("Femur Load (Left Front Seat)")
        # ax2.grid(True)
        fig.suptitle(f"Femur Load Value ({name})")
        plt.xlabel("Year")
        fig.savefig(os.path.join("Results", name, str(time.time()) + ".png"))
        plt.close()

        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        ax1.scatter(year, f_prob_1, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, f_prob_1)
            ax1.plot(np.array(year), m * np.array(year) + c, color=regColor)
        ax1.set_ylabel("" r"$\rho$ (Right Front Seat)")
        # ax1.grid(True)
        ax2.scatter(year, f_prob_2, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, f_prob_2)
            ax2.plot(np.array(year), m * np.array(year) + c, color=regColor)
        ax2.set_ylabel("" r"$\rho$ (Left Front Seat)")
        # ax2.grid(True)
        fig.suptitle(f"Femur Injury Probability ({name})")
        plt.xlabel("Year")
        fig.savefig(os.path.join("Results", name, str(time.time()) + ".png"))
        plt.close()

        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        ax1.scatter(year, nfa_1, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, nfa_1)
            ax1.plot(np.array(year), m * np.array(year) + c, color=regColor)
        ax1.set_ylabel("N$_f$$_a$ (Right Front Seat)")
        # ax1.grid(True)
        ax2.scatter(year, nfa_2, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, nfa_2)
            ax2.plot(np.array(year), m * np.array(year) + c, color=regColor)
        ax2.set_ylabel("N$_f$$_a$ (Left Front Seat)")
        # ax2.grid(True)
        fig.suptitle(f"N$_f$$_a$ ({name})")
        plt.xlabel("Year")
        fig.savefig(os.path.join("Results", name, str(time.time()) + ".png"))
        plt.close()

        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        ax1.scatter(year, nea_1, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, nea_1)
            ax1.plot(np.array(year), m * np.array(year) + c, color=regColor)
        ax1.set_ylabel("N$_e$$_a$ (Right Front Seat)")
        # ax1.grid(True)
        ax2.scatter(year, nea_2, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, nea_2)
            ax2.plot(np.array(year), m * np.array(year) + c, color=regColor)
        ax2.set_ylabel("N$_e$$_a$ (Left Front Seat)")
        # ax2.grid(True)
        fig.suptitle(f"N$_e$$_a$ ({name})")
        plt.xlabel("Year")
        fig.savefig(os.path.join("Results", name, str(time.time()) + ".png"))
        plt.close()

        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        ax1.scatter(year, nfp_1, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, nfp_1)
            ax1.plot(np.array(year), m * np.array(year) + c, color=regColor)
        ax1.set_ylabel("N$_f$$_p$ (Right Front Seat)")
        # ax1.grid(True)
        ax2.scatter(year, nfp_2, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, nfp_2)
            ax2.plot(np.array(year), m * np.array(year) + c, color=regColor)
        ax2.set_ylabel("N$_f$$_p$ (Left Front Seat)")
        # ax2.grid(True)
        fig.suptitle(f"N$_f$$_p$ ({name})")
        plt.xlabel("Year")
        fig.savefig(os.path.join("Results", name, str(time.time()) + ".png"))
        plt.close()

        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        ax1.scatter(year, nep_1, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, nep_1)
            ax1.plot(np.array(year), m * np.array(year) + c, color=regColor)
        ax1.set_ylabel("N$_e$$_p$ (Right Front Seat)")
        # ax1.grid(True)
        ax2.scatter(year, nep_2, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, nep_2)
            ax2.plot(np.array(year), m * np.array(year) + c, color=regColor)
        ax2.set_ylabel("N$_e$$_p$ (Left Front Seat)")
        # ax2.grid(True)
        fig.suptitle(f"N$_e$$_p$ ({name})")
        plt.xlabel("Year")
        fig.savefig(os.path.join("Results", name, str(time.time()) + ".png"))
        plt.close()

        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        ax1.scatter(year, nkmm_1, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, nkmm_1)
            ax1.plot(np.array(year), m * np.array(year) + c, color=regColor)
        ax1.set_ylabel("N$_k$$_m$ (Right Front Seat)")
        # ax1.grid(True)
        ax2.scatter(year, nkmm_2, s=10, c=colors)
        if regres:
            m, c = plotRegression(year, nkmm_2)
            ax2.plot(np.array(year), m * np.array(year) + c, color=regColor)
        ax2.set_ylabel("N$_k$$_m$ (Left Front Seat)")
        # ax2.grid(True)
        fig.suptitle(f"N$_k$$_m$$^m$$^a$$^x$ ({name})")
        plt.xlabel("Year")
        fig.savefig(os.path.join("Results", name, str(time.time()) + ".png"))
        plt.close()

    elif pltType == "line":
        for item in ddata:
            year.append(int(item[0]))
            gsi_1.append(item[1]["gsi"] if not item[1]["gsi"] == None else 0)
            hic_1.append(item[1]["hic"] if not item[1]["hic"] == None else 0)
            prob_head_1.append(
                item[1]["prob_head"] if not item[1]["prob_head"] == None else 0
            )
            ms3_1.append(item[1]["ms3"] if not item[1]["ms3"] == None else 0)
            cti_1.append(item[1]["cti"] if not item[1]["cti"] == None else 0)
            csi_1.append(item[1]["csi"] if not item[1]["csi"] == None else 0)
            f_val_1.append(item[1]["fval"] if not item[1]["fval"] == None else 0)
            f_prob_1.append(item[1]["f_prob"] if not item[1]["f_prob"] == None else 0)
            f_flag_1.append(item[1]["f_flag"] if not item[1]["f_flag"] == None else 0)
            gsi_2.append(item[2]["gsi"] if not item[2]["gsi"] == None else 0)
            hic_2.append(item[2]["hic"] if not item[2]["hic"] == None else 0)
            prob_head_2.append(
                item[2]["prob_head"] if not item[2]["prob_head"] == None else 0
            )
            ms3_2.append(item[2]["ms3"] if not item[2]["ms3"] == None else 0)
            cti_2.append(item[2]["cti"] if not item[2]["cti"] == None else 0)
            csi_2.append(item[2]["csi"] if not item[2]["csi"] == None else 0)
            f_val_2.append(item[2]["fval"] if not item[2]["fval"] == None else 0)
            f_prob_2.append(item[2]["f_prob"] if not item[2]["f_prob"] == None else 0)
            f_flag_2.append(item[2]["f_flag"] if not item[2]["f_flag"] == None else 0)

        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        ax1.plot(year, gsi_1, marker="o")
        ax1.set_ylabel("GSI (Right Front Seat)")
        # ax1.grid(True)
        ax2.plot(year, gsi_2, marker="o")
        ax2.set_ylabel("GSI (Left Front Seat)")
        # ax2.grid(True)
        fig.suptitle(f"GSI ({name})")
        plt.xlabel("Year")
        fig.savefig(os.path.join("Results", name, str(time.time()) + ".png"))
        plt.close()

        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        ax1.plot(year, hic_1, marker="o")
        ax1.set_ylabel("HIC (Right Front Seat)")
        # ax1.grid(True)
        ax2.plot(year, hic_2, marker="o")
        ax2.set_ylabel("HIC (Left Front Seat)")
        # ax2.grid(True)
        fig.suptitle(f"HIC ({name})")
        plt.xlabel("Year")
        fig.savefig(os.path.join("Results", name, str(time.time()) + ".png"))
        plt.close()

        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        ax1.plot(year, prob_head_1, marker="o")
        ax1.set_ylabel("" r"$\rho$ (Right Front Seat)")
        # ax1.grid(True)
        ax2.plot(year, prob_head_2, marker="o")
        ax2.set_ylabel("" r"$\rho$ (Left Front Seat)")
        # ax2.grid(True)
        fig.suptitle(f"Head Fracture Probability ({name})")
        plt.xlabel("Year")
        fig.savefig(os.path.join("Results", name, str(time.time()) + ".png"))
        plt.close()

        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        ax1.plot(year, ms3_1, marker="o")
        ax1.set_ylabel("3ms (Right Front Seat)")
        # ax1.grid(True)
        ax2.plot(year, ms3_2, marker="o")
        ax2.set_ylabel("3ms (Left Front Seat)")
        # ax2.grid(True)
        fig.suptitle(f"3ms Criterion ({name})")
        plt.xlabel("Year")
        fig.savefig(os.path.join("Results", name, str(time.time()) + ".png"))
        plt.close()

        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        ax1.plot(year, cti_1, marker="o")
        ax1.set_ylabel("CTI (Right Front Seat)")
        # ax1.grid(True)
        ax2.plot(year, cti_2, marker="o")
        ax2.set_ylabel("CTI (Left Front Seat)")
        # ax2.grid(True)
        fig.suptitle(f"CTI ({name})")
        plt.xlabel("Year")
        fig.savefig(os.path.join("Results", name, str(time.time()) + ".png"))
        plt.close()

        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        ax1.plot(year, csi_1, marker="o")
        ax1.set_ylabel("CSI (Right Front Seat)")
        # ax1.grid(True)
        ax2.plot(year, csi_2, marker="o")
        ax2.set_ylabel("CSI (Left Front Seat)")
        # ax2.grid(True)
        fig.suptitle(f"CSI ({name})")
        plt.xlabel("Year")
        fig.savefig(os.path.join("Results", name, str(time.time()) + ".png"))
        plt.close()

        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        ax1.plot(year, f_val_1, marker="o")
        ax1.set_ylabel("Femur Load (Right Front Seat)")
        # ax1.grid(True)
        ax2.plot(year, f_val_2, marker="o")
        ax2.set_ylabel("Femur Load (Left Front Seat)")
        # ax2.grid(True)
        fig.suptitle(f"Femur Load Value ({name})")
        plt.xlabel("Year")
        fig.savefig(os.path.join("Results", name, str(time.time()) + ".png"))
        plt.close()

        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        ax1.plot(year, f_prob_1, marker="o")
        ax1.set_ylabel("" r"$\rho$ (Right Front Seat)")
        # ax1.grid(True)
        ax2.plot(year, f_prob_2, marker="o")
        ax2.set_ylabel("" r"$\rho$ (Left Front Seat)")
        # ax2.grid(True)
        fig.suptitle(f"Femur Injury Probability ({name})")
        plt.xlabel("Year")
        fig.savefig(os.path.join("Results", name, str(time.time()) + ".png"))
        plt.close()


base_path = os.path.dirname(os.path.realpath(sys.argv[0]))
dir_path = "NHTSA"

if os.path.exists(os.path.join(base_path, "Results")):
    shutil.rmtree(os.path.join(base_path, "Results"))

"""
*****************************************************************************
=========================== Extracting  Meta Data ===========================
*****************************************************************************
"""

data_files = os.listdir(dir_path)



print(f"{len(data_files)} files Found in Total!\n")

data = []
for itr, file in enumerate(data_files):
    if 'v' in file:
        data.append(procFile.getFileInfo(dirPath=os.path.join(dir_path, file)))

"""
*****************************************************************************
============================== Filtering  Data ==============================
*****************************************************************************
"""

log_file = os.path.join(base_path, "exceptions.log")
logger = logging.getLogger("my_logger")
handler = logging.FileHandler(log_file, mode="w")
logger.addHandler(handler)
logger.setLevel(logging.ERROR)

for itr, myDict in enumerate(tqdm(data)):
    """============ Right Front Seat Data Filter ============"""
    myDict["data_01"] = {}
    myDict["info_01"] = {}

    # Head CG Acceleration Filer
    myDict["data_01"]["hdcg_acc"] = procFile.filterData(
        data=myDict["instrument"],
        sensorAttachment="HDCG",
        sensorLocation="01",
        yUnits="G'S",
    )
    try:
        myDict["info_01"]["hdcg_acc"] = {}
        for j, file in enumerate(myDict["data_01"]["hdcg_acc"]["fileName"]):
            myDict["info_01"]["hdcg_acc"].update(
                {
                    f"{myDict['data_01']['hdcg_acc']['axis'][j]}": procFile.getSensorData(
                        filePath=os.path.join(myDict["file"], file)
                    )
                }
            )
    except TypeError:
        logger.error(f"Data not found at {itr+1} --> {myDict['file']}/01/HDCG_ACC")
        myDict["info_01"]["hdcg_acc"] = None

    # Chest Acceleration Filer
    myDict["data_01"]["chst_acc"] = procFile.filterData(
        data=myDict["instrument"],
        sensorAttachment="CHST",
        sensorLocation="01",
        yUnits="G'S",
    )
    try:
        myDict["info_01"]["chst_acc"] = {}
        for j, file in enumerate(myDict["data_01"]["chst_acc"]["fileName"]):
            myDict["info_01"]["chst_acc"].update(
                {
                    f"{myDict['data_01']['chst_acc']['axis'][j]}": procFile.getSensorData(
                        filePath=os.path.join(myDict["file"], file)
                    )
                }
            )
    except TypeError:
        logger.error(f"Data not found at {itr+1} --> {myDict['file']}/01/CHST_ACC")
        myDict["info_01"]["chst_acc"] = None

    # Chest Acceleration Deflection
    myDict["data_01"]["chst_def"] = procFile.filterData(
        data=myDict["instrument"],
        sensorAttachment="CHST",
        sensorLocation="01",
        yUnits="MM",
    )
    try:
        myDict["info_01"]["chst_def"] = {}
        for j, file in enumerate(myDict["data_01"]["chst_def"]["fileName"]):
            myDict["info_01"]["chst_def"].update(
                {
                    f"{myDict['data_01']['chst_def']['axis'][j]}": procFile.getSensorData(
                        filePath=os.path.join(myDict["file"], file)
                    )
                }
            )
    except TypeError:
        logger.error(f"Data not found at {itr+1} --> {myDict['file']}/01/CHST_DEF")
        myDict["info_01"]["chst_def"] = None

    # Femur Force
    myDict["data_01"]["fmrr_f"] = procFile.filterData(
        data=myDict["instrument"],
        sensorAttachment="FMRR",
        sensorLocation="01",
        yUnits="NWT",
    )
    myDict["data_01"]["fmrl_f"] = procFile.filterData(
        data=myDict["instrument"],
        sensorAttachment="FMRL",
        sensorLocation="01",
        yUnits="NWT",
    )
    try:
        myDict["info_01"]["fmrr_f"] = {}
        for j, file in enumerate(myDict["data_01"]["fmrr_f"]["fileName"]):
            myDict["info_01"]["fmrr_f"].update(
                {
                    f"{myDict['data_01']['fmrr_f']['axis'][j]}": procFile.getSensorData(
                        filePath=os.path.join(myDict["file"], file)
                    )
                }
            )
    except TypeError:
        logger.error(f"Data not found at {itr+1} --> {myDict['file']}/01/FMRR_F")
        myDict["info_01"]["fmrr_f"] = None
    try:
        myDict["info_01"]["fmrl_f"] = {}
        for j, file in enumerate(myDict["data_01"]["fmrl_f"]["fileName"]):
            myDict["info_01"]["fmrl_f"].update(
                {
                    f"{myDict['data_01']['fmrl_f']['axis'][j]}": procFile.getSensorData(
                        filePath=os.path.join(myDict["file"], file)
                    )
                }
            )
    except TypeError:
        logger.error(f"Data not found at {itr+1} --> {myDict['file']}/01/FMRL_F")
        myDict["info_01"]["fmrl_f"] = None

    # Upper Neck Forces
    myDict["data_01"]["neku_f"] = procFile.filterData(
        data=myDict["instrument"],
        sensorAttachment="NEKU",
        sensorLocation="01",
        yUnits="NWT",
    )
    try:
        myDict["info_01"]["neku_f"] = {}
        for j, file in enumerate(myDict["data_01"]["neku_f"]["fileName"]):
            myDict["info_01"]["neku_f"].update(
                {
                    f"{myDict['data_01']['neku_f']['axis'][j]}": procFile.getSensorData(
                        filePath=os.path.join(myDict["file"], file)
                    )
                }
            )
    except TypeError:
        logger.error(f"Data not found at {itr+1} --> {myDict['file']}/01/neku_f")
        myDict["info_01"]["neku_f"] = None

    # Upper Neck Moments
    myDict["data_01"]["neku_m"] = procFile.filterData(
        data=myDict["instrument"],
        sensorAttachment="NEKU",
        sensorLocation="01",
        yUnits="NWM",
    )
    try:
        myDict["info_01"]["neku_m"] = {}
        for j, file in enumerate(myDict["data_01"]["neku_m"]["fileName"]):
            myDict["info_01"]["neku_m"].update(
                {
                    f"{myDict['data_01']['neku_m']['axis'][j]}": procFile.getSensorData(
                        filePath=os.path.join(myDict["file"], file)
                    )
                }
            )
    except TypeError:
        logger.error(f"Data not found at {itr+1} --> {myDict['file']}/01/neku_m")
        myDict["info_01"]["neku_m"] = None

    """============ Left Front Seat Data Filter ============"""
    myDict["data_02"] = {}
    myDict["info_02"] = {}

    # Head CG Acceleration Filer
    myDict["data_02"]["hdcg_acc"] = procFile.filterData(
        data=myDict["instrument"],
        sensorAttachment="HDCG",
        sensorLocation="02",
        yUnits="G'S",
    )
    try:
        myDict["info_02"]["hdcg_acc"] = {}
        for j, file in enumerate(myDict["data_02"]["hdcg_acc"]["fileName"]):
            myDict["info_02"]["hdcg_acc"].update(
                {
                    f"{myDict['data_02']['hdcg_acc']['axis'][j]}": procFile.getSensorData(
                        filePath=os.path.join(myDict["file"], file)
                    )
                }
            )
    except TypeError:
        logger.error(f"Data not found at {itr+1} --> {myDict['file']}/02/HDCG_ACC")
        myDict["info_02"]["hdcg_acc"] = None

    # Chest Acceleration Filer
    myDict["data_02"]["chst_acc"] = procFile.filterData(
        data=myDict["instrument"],
        sensorAttachment="CHST",
        sensorLocation="02",
        yUnits="G'S",
    )
    try:
        myDict["info_02"]["chst_acc"] = {}
        for j, file in enumerate(myDict["data_02"]["chst_acc"]["fileName"]):
            myDict["info_02"]["chst_acc"].update(
                {
                    f"{myDict['data_02']['chst_acc']['axis'][j]}": procFile.getSensorData(
                        filePath=os.path.join(myDict["file"], file)
                    )
                }
            )
    except TypeError:
        logger.error(f"Data not found at {itr+1} --> {myDict['file']}/02/CHST_ACC")
        myDict["info_02"]["chst_acc"] = None

    # Chest Deflection Filer
    myDict["data_02"]["chst_def"] = procFile.filterData(
        data=myDict["instrument"],
        sensorAttachment="CHST",
        sensorLocation="02",
        yUnits="MM",
    )
    try:
        myDict["info_02"]["chst_def"] = {}
        for j, file in enumerate(myDict["data_02"]["chst_def"]["fileName"]):
            myDict["info_02"]["chst_def"].update(
                {
                    f"{myDict['data_02']['chst_def']['axis'][j]}": procFile.getSensorData(
                        filePath=os.path.join(myDict["file"], file)
                    )
                }
            )
    except TypeError:
        logger.error(f"Data not found at {itr+1} --> {myDict['file']}/02/CHST_DEF")
        myDict["info_02"]["chst_def"] = None

    # Femur Force
    myDict["data_02"]["fmrr_f"] = procFile.filterData(
        data=myDict["instrument"],
        sensorAttachment="FMRR",
        sensorLocation="02",
        yUnits="NWT",
    )
    myDict["data_02"]["fmrl_f"] = procFile.filterData(
        data=myDict["instrument"],
        sensorAttachment="FMRL",
        sensorLocation="02",
        yUnits="NWT",
    )
    try:
        myDict["info_02"]["fmrr_f"] = {}
        for j, file in enumerate(myDict["data_02"]["fmrr_f"]["fileName"]):
            myDict["info_02"]["fmrr_f"].update(
                {
                    f"{myDict['data_02']['fmrr_f']['axis'][j]}": procFile.getSensorData(
                        filePath=os.path.join(myDict["file"], file)
                    )
                }
            )
    except TypeError:
        logger.error(f"Data not found at {itr+1} --> {myDict['file']}/02/FMRR_F")
        myDict["info_02"]["fmrr_f"] = None
    try:
        myDict["info_02"]["fmrl_f"] = {}
        for j, file in enumerate(myDict["data_02"]["fmrl_f"]["fileName"]):
            myDict["info_02"]["fmrl_f"].update(
                {
                    f"{myDict['data_02']['fmrl_f']['axis'][j]}": procFile.getSensorData(
                        filePath=os.path.join(myDict["file"], file)
                    )
                }
            )
    except TypeError:
        logger.error(f"Data not found at {itr+1} --> {myDict['file']}/02/FMRL_F")
        myDict["info_02"]["fmrl_f"] = None

    # Upper Neck Forces
    myDict["data_02"]["neku_f"] = procFile.filterData(
        data=myDict["instrument"],
        sensorAttachment="NEKU",
        sensorLocation="02",
        yUnits="NWT",
    )
    try:
        myDict["info_02"]["neku_f"] = {}
        for j, file in enumerate(myDict["data_02"]["neku_f"]["fileName"]):
            myDict["info_02"]["neku_f"].update(
                {
                    f"{myDict['data_02']['neku_f']['axis'][j]}": procFile.getSensorData(
                        filePath=os.path.join(myDict["file"], file)
                    )
                }
            )
    except TypeError:
        logger.error(f"Data not found at {itr+1} --> {myDict['file']}/02/neku_f")
        myDict["info_02"]["neku_f"] = None

    # Upper Neck Moments
    myDict["data_02"]["neku_m"] = procFile.filterData(
        data=myDict["instrument"],
        sensorAttachment="NEKU",
        sensorLocation="02",
        yUnits="NWM",
    )
    try:
        myDict["info_02"]["neku_m"] = {}
        for j, file in enumerate(myDict["data_02"]["neku_m"]["fileName"]):
            myDict["info_02"]["neku_m"].update(
                {
                    f"{myDict['data_02']['neku_m']['axis'][j]}": procFile.getSensorData(
                        filePath=os.path.join(myDict["file"], file)
                    )
                }
            )
    except TypeError:
        logger.error(f"Data not found at {itr+1} --> {myDict['file']}/02/neku_m")
        myDict["info_02"]["neku_m"] = None

handler.close()

"""
*****************************************************************************
============================== Analyzing  Data ==============================
*****************************************************************************
"""

for itr, myDict in enumerate(tqdm(data)):
    """============ Right Front Seat Data Filter ============"""
    myDict["proc_01"] = {}

    try:
        keys = list(myDict["info_01"]["hdcg_acc"].keys())
        myDict["proc_01"]["gsi"] = analysis.calGSI(
            ax=np.array(myDict["info_01"]["hdcg_acc"][f"{keys[0]}"][1]),
            ay=np.array(myDict["info_01"]["hdcg_acc"][f"{keys[1]}"][1]),
            az=np.array(myDict["info_01"]["hdcg_acc"][f"{keys[2]}"][1]),
            t=np.array(myDict["info_01"]["hdcg_acc"][f"{keys[2]}"][0]),
        )
    except:
        myDict["proc_01"]["gsi"] = None

    try:
        myDict["proc_01"]["hic"], myDict["proc_01"]["prob_head"] = analysis.calHIC(
            ax=np.array(myDict["info_01"]["hdcg_acc"][f"{keys[0]}"][1]),
            ay=np.array(myDict["info_01"]["hdcg_acc"][f"{keys[1]}"][1]),
            az=np.array(myDict["info_01"]["hdcg_acc"][f"{keys[2]}"][1]),
            t=np.array(myDict["info_01"]["hdcg_acc"][f"{keys[2]}"][0]),
        )
    except:
        myDict["proc_01"]["hic"] = None
        myDict["proc_01"]["prob_head"] = None
        
    try:
        myDict["proc_01"]["hic36"], myDict["proc_01"]["prob_head36"] = analysis.calHIC(
            ax=np.array(myDict["info_01"]["hdcg_acc"][f"{keys[0]}"][1]),
            ay=np.array(myDict["info_01"]["hdcg_acc"][f"{keys[1]}"][1]),
            az=np.array(myDict["info_01"]["hdcg_acc"][f"{keys[2]}"][1]),
            t=np.array(myDict["info_01"]["hdcg_acc"][f"{keys[2]}"][0]),
            opt='HIC36'
        )
    except:
        myDict["proc_01"]["hic36"] = None
        myDict["proc_01"]["prob_head36"] = None
        
    try:
        myDict["proc_01"]["hic15"], myDict["proc_01"]["prob_head15"] = analysis.calHIC(
            ax=np.array(myDict["info_01"]["hdcg_acc"][f"{keys[0]}"][1]),
            ay=np.array(myDict["info_01"]["hdcg_acc"][f"{keys[1]}"][1]),
            az=np.array(myDict["info_01"]["hdcg_acc"][f"{keys[2]}"][1]),
            t=np.array(myDict["info_01"]["hdcg_acc"][f"{keys[2]}"][0]),
            opt='HIC15'
        )
    except:
        myDict["proc_01"]["hic15"] = None
        myDict["proc_01"]["prob_head15"] = None
        
    try:
        myDict["proc_01"]["ms3h"] = analysis.calc3ms(
            ax=np.array(myDict["info_01"]["hdcg_acc"][f"{keys[0]}"][1]),
            ay=np.array(myDict["info_01"]["hdcg_acc"][f"{keys[1]}"][1]),
            az=np.array(myDict["info_01"]["hdcg_acc"][f"{keys[2]}"][1]),
            t=np.array(myDict["info_01"]["hdcg_acc"][f"{keys[2]}"][0]),
            tol=80
        )
    except:
        myDict["proc_01"]["ms3h"] = None

    try:
        keys = list(myDict["info_01"]["chst_acc"].keys())
        myDict["proc_01"]["ms3"] = analysis.calc3ms(
            ax=np.array(myDict["info_01"]["chst_acc"][f"{keys[0]}"][1]),
            ay=np.array(myDict["info_01"]["chst_acc"][f"{keys[1]}"][1]),
            az=np.array(myDict["info_01"]["chst_acc"][f"{keys[2]}"][1]),
            t=np.array(myDict["info_01"]["chst_acc"][f"{keys[2]}"][0]),
        )
    except:
        myDict["proc_01"]["ms3"] = None

    try:
        myDict["proc_01"]["csi"] = analysis.calcCSI(
            ax=np.array(myDict["info_01"]["chst_acc"][f"{keys[0]}"][1]),
            ay=np.array(myDict["info_01"]["chst_acc"][f"{keys[1]}"][1]),
            az=np.array(myDict["info_01"]["chst_acc"][f"{keys[2]}"][1]),
            t=np.array(myDict["info_01"]["chst_acc"][f"{keys[2]}"][0]),
        )
    except:
        myDict["proc_01"]["csi"] = None

    try:
        keys = list(myDict["info_01"]["chst_def"].keys())
        myDict["proc_01"]["cti"] = analysis.calcCTI(
            ms3=myDict["proc_01"]["ms3"],
            D=np.array(myDict["info_01"]["chst_def"][f"{keys[0]}"][1]),
        )
    except:
        myDict["proc_01"]["cti"] = None

    try:
        keys_l = list(myDict["info_01"]["fmrl_f"].keys())
        keys_r = list(myDict["info_01"]["fmrr_f"].keys())
        (
            myDict["proc_01"]["fval"],
            myDict["proc_01"]["f_flag"],
            myDict["proc_01"]["f_prob"],
        ) = analysis.calcFemurLoad(
            f=np.average(
                [
                    myDict["info_01"]["fmrl_f"][f"{keys_l[0]}"][1],
                    myDict["info_01"]["fmrr_f"][f"{keys_r[0]}"][1],
                ],
                0,
            )
        )
    except:
        try:
            keys_l = list(myDict["info_01"]["fmrl_f"].keys())
            (
                myDict["proc_01"]["fval"],
                myDict["proc_01"]["f_flag"],
                myDict["proc_01"]["f_prob"],
            ) = analysis.calcFemurLoad(f=myDict["info_01"]["fmrl_f"][f"{keys_l[0]}"][1])
        except:
            try:
                keys_r = list(myDict["info_01"]["fmrr_f"].keys())
                (
                    myDict["proc_01"]["fval"],
                    myDict["proc_01"]["f_flag"],
                    myDict["proc_01"]["f_prob"],
                ) = analysis.calcFemurLoad(
                    f=myDict["info_01"]["fmrr_f"][f"{keys_r[0]}"][1]
                )
            except:
                myDict["proc_01"]["fval"] = None
                myDict["proc_01"]["f_flag"] = None
                myDict["proc_01"]["f_prob"] = None

    try:
        keys_f = list(myDict["info_01"]["neku_f"].keys())
        keys_m = list(myDict["info_01"]["neku_m"].keys())
        (
            myDict["proc_01"]["nfa"],
            myDict["proc_01"]["nea"],
            myDict["proc_01"]["nfp"],
            myDict["proc_01"]["nep"],
        ) = analysis.calcNkm(
            fx=np.array(myDict["info_01"]["neku_f"][f"{keys_f[0]}"][1]),
            my=np.array(myDict["info_01"]["neku_m"][f"{keys_m[1]}"][1]),
            t=np.array(myDict["info_01"]["neku_m"][f"{keys_m[1]}"][0]),
        )
    except:
        myDict["proc_01"]["nfa"] = myDict["proc_01"]["nea"] = myDict["proc_01"][
            "nfp"
        ] = myDict["proc_01"]["nep"] = None

    """============ Left Front Seat Data Filter ============"""
    myDict["proc_02"] = {}

    try:
        keys = list(myDict["info_02"]["hdcg_acc"].keys())
        myDict["proc_02"]["gsi"] = analysis.calGSI(
            ax=np.array(myDict["info_02"]["hdcg_acc"][f"{keys[0]}"][1]),
            ay=np.array(myDict["info_02"]["hdcg_acc"][f"{keys[1]}"][1]),
            az=np.array(myDict["info_02"]["hdcg_acc"][f"{keys[2]}"][1]),
            t=np.array(myDict["info_02"]["hdcg_acc"][f"{keys[2]}"][0]),
        )
    except:
        myDict["proc_02"]["gsi"] = None

    try:
        myDict["proc_02"]["hic"], myDict["proc_02"]["prob_head"] = analysis.calHIC(
            ax=np.array(myDict["info_02"]["hdcg_acc"][f"{keys[0]}"][1]),
            ay=np.array(myDict["info_02"]["hdcg_acc"][f"{keys[1]}"][1]),
            az=np.array(myDict["info_02"]["hdcg_acc"][f"{keys[2]}"][1]),
            t=np.array(myDict["info_02"]["hdcg_acc"][f"{keys[2]}"][0]),
        )
    except:
        myDict["proc_02"]["hic"] = None
        myDict["proc_02"]["prob_head"] = None
        
    try:
        myDict["proc_02"]["hic36"], myDict["proc_02"]["prob_head36"] = analysis.calHIC(
            ax=np.array(myDict["info_02"]["hdcg_acc"][f"{keys[0]}"][1]),
            ay=np.array(myDict["info_02"]["hdcg_acc"][f"{keys[1]}"][1]),
            az=np.array(myDict["info_02"]["hdcg_acc"][f"{keys[2]}"][1]),
            t=np.array(myDict["info_02"]["hdcg_acc"][f"{keys[2]}"][0]),
            opt='HIC36'
        )
    except:
        myDict["proc_02"]["hic36"] = None
        myDict["proc_02"]["prob_head36"] = None
        
    try:
        myDict["proc_02"]["hic15"], myDict["proc_02"]["prob_head15"] = analysis.calHIC(
            ax=np.array(myDict["info_02"]["hdcg_acc"][f"{keys[0]}"][1]),
            ay=np.array(myDict["info_02"]["hdcg_acc"][f"{keys[1]}"][1]),
            az=np.array(myDict["info_02"]["hdcg_acc"][f"{keys[2]}"][1]),
            t=np.array(myDict["info_02"]["hdcg_acc"][f"{keys[2]}"][0]),
            opt='HIC15'
        )
    except:
        myDict["proc_02"]["hic15"] = None
        myDict["proc_02"]["prob_head15"] = None
        
    try:
        myDict["proc_02"]["ms3h"] = analysis.calc3ms(
            ax=np.array(myDict["info_02"]["hdcg_acc"][f"{keys[0]}"][1]),
            ay=np.array(myDict["info_02"]["hdcg_acc"][f"{keys[1]}"][1]),
            az=np.array(myDict["info_02"]["hdcg_acc"][f"{keys[2]}"][1]),
            t=np.array(myDict["info_02"]["hdcg_acc"][f"{keys[2]}"][0]),
            tol=80
        )
    except:
        myDict["proc_02"]["ms3h"] = None

    try:
        keys = list(myDict["info_02"]["chst_acc"].keys())
        myDict["proc_02"]["ms3"] = analysis.calc3ms(
            ax=np.array(myDict["info_02"]["chst_acc"][f"{keys[0]}"][1]),
            ay=np.array(myDict["info_02"]["chst_acc"][f"{keys[1]}"][1]),
            az=np.array(myDict["info_02"]["chst_acc"][f"{keys[2]}"][1]),
            t=np.array(myDict["info_02"]["chst_acc"][f"{keys[2]}"][0]),
        )
    except:
        myDict["proc_02"]["ms3"] = None

    try:
        myDict["proc_02"]["csi"] = analysis.calcCSI(
            ax=np.array(myDict["info_02"]["chst_acc"][f"{keys[0]}"][1]),
            ay=np.array(myDict["info_02"]["chst_acc"][f"{keys[1]}"][1]),
            az=np.array(myDict["info_02"]["chst_acc"][f"{keys[2]}"][1]),
            t=np.array(myDict["info_02"]["chst_acc"][f"{keys[2]}"][0]),
        )
    except:
        myDict["proc_02"]["csi"] = None

    try:
        keys = list(myDict["info_02"]["chst_def"].keys())
        myDict["proc_02"]["cti"] = analysis.calcCTI(
            ms3=myDict["proc_02"]["ms3"],
            D=np.array(myDict["info_02"]["chst_def"][f"{keys[0]}"][1]),
        )
    except:
        myDict["proc_02"]["cti"] = None

    try:
        keys_l = list(myDict["info_02"]["fmrl_f"].keys())
        keys_r = list(myDict["info_02"]["fmrr_f"].keys())
        (
            myDict["proc_02"]["fval"],
            myDict["proc_02"]["f_flag"],
            myDict["proc_02"]["f_prob"],
        ) = analysis.calcFemurLoad(
            f=np.average(
                [
                    myDict["info_02"]["fmrl_f"][f"{keys_l[0]}"][1],
                    myDict["info_02"]["fmrr_f"][f"{keys_r[0]}"][1],
                ],
                0,
            )
        )
    except:
        try:
            keys_l = list(myDict["info_02"]["fmrl_f"].keys())
            (
                myDict["proc_02"]["fval"],
                myDict["proc_02"]["f_flag"],
                myDict["proc_02"]["f_prob"],
            ) = analysis.calcFemurLoad(f=myDict["info_02"]["fmrl_f"][f"{keys_l[0]}"][1])
        except:
            try:
                keys_r = list(myDict["info_02"]["fmrr_f"].keys())
                (
                    myDict["proc_02"]["fval"],
                    myDict["proc_02"]["f_flag"],
                    myDict["proc_02"]["f_prob"],
                ) = analysis.calcFemurLoad(
                    f=myDict["info_02"]["fmrr_f"][f"{keys_r[0]}"][1]
                )
            except:
                myDict["proc_02"]["fval"] = None
                myDict["proc_02"]["f_flag"] = None
                myDict["proc_02"]["f_prob"] = None

    try:
        keys_f = list(myDict["info_02"]["neku_f"].keys())
        keys_m = list(myDict["info_02"]["neku_m"].keys())
        (
            myDict["proc_02"]["nfa"],
            myDict["proc_02"]["nea"],
            myDict["proc_02"]["nfp"],
            myDict["proc_02"]["nep"],
        ) = analysis.calcNkm(
            fx=np.array(myDict["info_02"]["neku_f"][f"{keys_f[0]}"][1]),
            my=np.array(myDict["info_02"]["neku_m"][f"{keys_m[1]}"][1]),
            t=np.array(myDict["info_02"]["neku_m"][f"{keys_m[1]}"][0]),
        )
    except:
        myDict["proc_02"]["nfa"] = myDict["proc_02"]["nea"] = myDict["proc_02"][
            "nfp"
        ] = myDict["proc_02"]["nep"] = None

"""
*****************************************************************************
============================= Plotting Analysis =============================
*****************************************************************************
"""

plotData(data, "All")

# arranged = getArranged(data)
# print('\nCars Models:')
# print(arranged)
# print('\n')
# arranged = [i[0] for i in arranged]

# cdata = {}

# for itr, myDict in enumerate(data):
#     nname = myDict['file'].split('_')[-2]
#     if nname in arranged:
#         try:
#             cdata[f'{nname}'].append(
#                 [myDict['date']['year'], myDict['proc_01'], myDict['proc_02']])
#         except:
#             cdata.update(
#                 {f'{nname}': [[myDict['date']['year'], myDict['proc_01'], myDict['proc_02']]]})

# for item in cdata:
#     cdata[f'{item}'].sort(key=lambda x: int(x[0]))

# for item in tqdm(arranged):
#     plotData(cdata[f'{item}'], f'{item.title()}', 'line')

print("\nDone!")
"""
==============================================================================
"""
