import numpy as np
from scipy import integrate
import scipy.stats as stats


def calGSI(ax, ay, az, t):
    """
    Calculate Gadd Severity Index (GSI)

    Args:
        ax (np.array): X-Component of acceleration at center of gravity of head {g}
        ay (np.array): Y-Component of acceleration at center of gravity of head {g}
        az (np.array): Z-Component of acceleration at center of gravity of head {g}
        t  (np.array): Time vector {s}

    Returns:
        gsi (np.float): GSI Value
    """

    t_idx = np.where(t == 0)

    t = t[t_idx[0][0] :]
    ax = ax[t_idx[0][0] :]
    ay = ay[t_idx[0][0] :]
    az = az[t_idx[0][0] :]

    ar = np.sqrt(ax**2 + ay**2 + az**2)

    try:
        # Calculate GSI
        gsi = integrate.trapezoid(ar ** (2.5), t)

        return gsi

    except Exception as e:
        print(f"Exception has Occurred: ''{e}''")
        return None


def calHIC(ax, ay, az, t, opt=None):
    """
    Calculate Head Injury Criteria (HIC)

    Args:
        ax (np.array): X-Component of acceleration at center of gravity of head {g}
        ay (np.array): Y-Component of acceleration at center of gravity of head {g}
        az (np.array): Z-Component of acceleration at center of gravity of head {g}
        t  (np.array): Time vector {s}

    Returns:
        hic  (np.float): HIC value
        prob (np.float): Skull fracture probability value
    """

    t_idx = np.where(t == 0)

    t = t[t_idx[0][0] :]
    ax = ax[t_idx[0][0] :]
    ay = ay[t_idx[0][0] :]
    az = az[t_idx[0][0] :]

    ar = np.sqrt(ax**2 + ay**2 + az**2)
    mu = 6.96352
    sigma = 0.84664

    if opt is not None:
        ar_max = np.max(ar)
        ar_max_idx = np.where(ar == ar_max)[0][0]
        td = abs(t[0] - t[1])
        if opt == "HIC36":
            try:
                t = t[
                    int(ar_max_idx - np.ceil(0.018 / td)) : int(
                        ar_max_idx + np.ceil(0.018 / td)
                    )
                    + 1
                ]
                ar = ar[
                    int(ar_max_idx - np.ceil(0.018 / td)) : int(
                        ar_max_idx + np.ceil(0.018 / td)
                    )
                    + 1
                ]
            except:
                if ar_max_idx > ar.shape[0] / 2:
                    idx_r = int(ar.shape[0] - ar_max_idx)
                    idx_l = int(np.ceil(0.036 / td) - idx_r)
                    t = t[ar_max_idx - idx_l : ar_max_idx + idx_r + 1]
                    ar = ar[ar_max_idx - idx_l : ar_max_idx + idx_r + 1]
                elif ar_max_idx < ar.shape[0] / 2:
                    idx_l = int(ar_max_idx)
                    idx_r = int(np.ceil(0.036 / td) - idx_l)
                    t = t[ar_max_idx - idx_l : ar_max_idx + idx_r + 1]
                    ar = ar[ar_max_idx - idx_l : ar_max_idx + idx_r + 1]
        elif opt == "HIC15":
            try:
                t = t[
                    int(ar_max_idx - np.ceil(0.0075 / td)) : int(
                        ar_max_idx + np.ceil(0.0075 / td)
                    )
                    + 1
                ]
                ar = ar[
                    int(ar_max_idx - np.ceil(0.0075 / td)) : int(
                        ar_max_idx + np.ceil(0.0075 / td)
                    )
                    + 1
                ]
            except:
                if ar_max_idx > ar.shape[0] / 2:
                    idx_r = int(ar.shape[0] - ar_max_idx)
                    idx_l = int(np.ceil(0.015 / td) - idx_r)
                    t = t[ar_max_idx - idx_l : ar_max_idx + idx_r + 1]
                    ar = ar[ar_max_idx - idx_l : ar_max_idx + idx_r + 1]
                elif ar_max_idx < ar.shape[0] / 2:
                    idx_l = int(ar_max_idx)
                    idx_r = int(np.ceil(0.015 / td) - idx_l)
                    t = t[ar_max_idx - idx_l : ar_max_idx + idx_r + 1]
                    ar = ar[ar_max_idx - idx_l : ar_max_idx + idx_r + 1]

    try:
        # Calculate HIC
        hic = (t[-1] - t[0]) * np.max(
            (1 / (t[-1] - t[0])) * integrate.trapezoid(ar, t)
        ) ** (2.5)

        # Calculate probability of skulls fracture
        prob = stats.norm.cdf((np.log(hic) - mu) / sigma)

        return hic, prob

    except Exception as e:
        print(f"Exception has Occurred: ''{e}''")
        return None


def calc3ms(ax, ay, az, t, tol=60):
    """
    Calculate 3ms Criterion

    Args:
        ax  (np.array): X-Component of acceleration at chest {g}
        ay  (np.array): Y-Component of acceleration at chest {g}
        az  (np.array): Z-Component of acceleration at chest {g}chest
        t   (np.array): Time vector {s}
        tol (np.float): 3ms Tolerance {g}

    Returns:
        ms3_val (np.float): 3ms Criterion value
    """

    t_idx = np.where(t == 0)

    t = t[t_idx[0][0] :]
    ax = ax[t_idx[0][0] :]
    ay = ay[t_idx[0][0] :]
    az = az[t_idx[0][0] :]

    td = np.abs(t[2] - t[1])
    ms3_val = 0

    try:
        ar = np.sqrt(ax**2 + ay**2 + az**2)
        for i, value in enumerate(ar):
            if value < tol and value > ms3_val:
                ms3_val = value

        # for i, value in enumerate(ar):
        #     if value <= tol:
        #         ms3_count += 1
        #     else:
        #         ms3_count = 0

        #     if ms3_count >= (3e-3/td) and value < ms3_val:
        #         ms3_val = value

        return ms3_val
    except Exception as e:
        print(f"Exception has Occurred: ''{e}''")
        return None


def calcCTI(ms3, D, A_int=85, D_int=102):
    """
    Calculate Combined Thoracic Index (CTI)

    Args:
        ms3   (np.float): 3ms Value {g}
        D     (np.array): Chest deflection vector {mm}
        A_int (np.float): Intercept value for the acceleration (85g Hybrid III 50th percentile dummy) [optional]
        D_int (np.float): Intercept value for the deflection (102mm Hybrid III 50th percentile dummy) [optional]

    Returns:
        cti (np.float): CTI value
    """

    cti = (ms3 / A_int) + (np.max(D) / D_int)
    return cti


def calcCSI(ax, ay, az, t):
    """
    Calculate Chest Severity Index (CSI)

    Args:
        ax  (np.array): X-Component of acceleration at chest {g}
        ay  (np.array): Y-Component of acceleration at chest {g}
        az  (np.array): Z-Component of acceleration at chest {g}chest
        t   (np.array): Time vector {s}

    Returns:
        csi (np.float): CSI value
    """

    t_idx = np.where(t == 0)

    t = t[t_idx[0][0] :]
    ax = ax[t_idx[0][0] :]
    ay = ay[t_idx[0][0] :]
    az = az[t_idx[0][0] :]

    try:
        ar = np.sqrt(ax**2 + ay**2 + az**2)
        csi = (integrate.trapezoid(ar, t)) ** (2.5)

        return csi
    except Exception as e:
        print(f"Exception has Occurred: ''{e}''")
        return None


def calcFemurLoad(f, tol=10):
    """
    Calculate Femur Load

    Args:
        f   (np.array): Femur force {KN}
        tol (np.float): Femur load tolerance {g}

    Returns:
        fl_val  (np.float): Femur load value
        fl_flag (bool): Tolerance flag
        prob (np.array): Probability of injury
    """

    fl_val = np.max(f)

    if fl_val > tol:
        fl_flag = True
    else:
        fl_flag = False

    prob = 1 / (1 + np.exp(5.795 - (0.5196 * (fl_val / 1000))))

    return fl_val, fl_flag, prob


def calcNkm(fx, my, t):
    def Nkm(f, m, fint, mint, time):
        nkm = (f / fint) + (m / mint)
        # return integrate.trapezoid(nkm, time)
        return nkm

    t_idx = np.where(t == 0)

    t = t[t_idx[0][0] :]
    fx = fx[t_idx[0][0] :]
    my = my[t_idx[0][0] :]

    nfa = Nkm(max(abs(fx)), max(abs(my)), 845, 88.1, t)
    nea = Nkm(max(abs(fx)), max(abs(my)), 845, 47.5, t)
    nfp = Nkm(max(abs(fx)), max(abs(my)), 845, 88.1, t)
    nep = Nkm(max(abs(fx)), max(abs(my)), 845, 47.5, t)

    return nfa, nea, nfp, nep
