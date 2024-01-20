import numpy as np


class Zone:
    def __init__(self, shape: str, low=None, up=None, center=None, r=None, verify_zone=None):
        self.shape = shape
        self.verify_zone = verify_zone
        if shape == 'ball':
            self.center = np.array(center, dtype=np.float32)
            self.r = r  # radius squared
        elif shape == 'box':
            self.low = np.array(low, dtype=np.float32)
            self.up = np.array(up, dtype=np.float32)
        else:
            raise ValueError(f'There is no area of such shape!')


class Example:
    def __init__(self, n, local_1, init, unsafe, f_1, name, local_2=None, guard_1=None, guard_2=None, reset_1=None,
                 reset_2=None, f_2=None, continuous=False):
        self.n = n  # number of variables
        self.l1 = local_1
        self.l2 = local_2
        self.I = init
        self.U = unsafe
        self.g1 = guard_1
        self.g2 = guard_2
        self.r1 = reset_1
        self.r2 = reset_2
        self.f1 = f_1
        self.f2 = f_2
        self.name = name  # name or identifier
        self.continuous = continuous


examples = {
    1: Example(
        n=2,
        local_1=Zone(shape='box', low=[-2, -2], up=[0, 2]),
        local_2=Zone(shape='box', low=[0, -2], up=[2, 2]),
        init=Zone(shape='ball', center=[-1, -1], r=0.5 ** 2),
        unsafe=Zone(shape='ball', center=[1, 1], r=0.5 ** 2),
        guard_1=Zone(shape='box', low=[0, -2], up=[2, 2]),
        guard_2=Zone(shape='box', low=[-2, -2], up=[0, 2]),
        reset_1=[lambda x: x[0], lambda x: x[1]],
        reset_2=[lambda x: x[0], lambda x: x[1]],
        f_1=[lambda x: x[1],
             lambda x: x[0] - 0.25 * x[0] ** 2],
        f_2=[lambda x: x[1],
             lambda x: -x[0] - 0.5 * x[0] ** 3],
        name='H1'
        # fossil
    ),
    2: Example(
        n=2,
        local_1=Zone(shape='box', low=[-5, -5], up=[0, 5], verify_zone=[lambda x: -x[0]]),
        local_2=Zone(shape='box', low=[0, -5], up=[5, 5], verify_zone=[lambda x: x[0]]),
        init=Zone(shape='ball', center=[-2, 2], r=0.5 ** 2),
        unsafe=Zone(shape='ball', center=[2, 2], r=0.5 ** 2),
        guard_1=Zone(shape='ball', center=[0, 0], r=0.75 ** 2),
        guard_2=Zone(shape='ball', center=[0, 0], r=0.5 ** 2),
        reset_1=[lambda x: -x[0], lambda x: x[1]],
        reset_2=[lambda x: x[0] - 2, lambda x: x[1] + 1],
        f_1=[lambda x: -x[0] + x[0] * x[1],
             lambda x: -x[1]],
        f_2=[lambda x: -x[0] + 2 * x[0] ** 2 * x[1],
             lambda x: -x[1]],
        name='H2'  # Safety Verification of Nonlinear Hybrid Systems Based on Bilinear Programming->H3
    ),
    3: Example(
        n=2,
        local_1=Zone(shape='box', low=[-5, -5], up=[0, 5]),
        local_2=Zone(shape='box', low=[0, -5], up=[5, 5]),
        init=Zone(shape='box', low=[-2, -2], up=[-1, -1]),
        unsafe=Zone(shape='box', low=[0, -2], up=[1, -1]),
        guard_1=Zone(shape='ball', center=[-0.5, -0.5], r=0.5 ** 2),
        guard_2=Zone(shape='ball', center=[1, 1], r=0.5 ** 2),
        reset_1=[lambda x: -x[0] + 2, lambda x: -x[1] + 2],
        reset_2=[lambda x: x[0] - 2, lambda x: x[1] - 2],
        f_1=[lambda x: x[0] - x[0] * x[1],
             lambda x: -x[1] + x[0] * x[1]],
        f_2=[lambda x: x[0] + x[0] ** 2 * x[1],
             lambda x: x[1] + x[0] * x[1]],
        name='H3'
        # Darboux-type_barrier_certificates_for_safety_verification_of_nonlinear_hybrid_systems->EXAMPLE2
    ),
    4: Example(
        n=3,
        local_1=Zone(shape='box', low=[-1.1, -11, -11], up=[1.1, 11, 11]),
        local_2=Zone(shape='box', low=[0.17, 0.17, 0.17], up=[12, 12, 12]),
        init=Zone(shape='ball', center=[0, 0, 0], r=0.01),
        unsafe=Zone(shape='box', low=[5, -100, -100], up=[5.1, 100, 100],
                    verify_zone=[lambda x: (x[0] - 5) * (5.1 - x[0])]),
        guard_1=Zone(shape='box', low=[0.99, 9.95, 9.95], up=[1.01, 10.05, 10.05]),
        guard_2=Zone(shape='box', low=[0.17] * 3, up=[0.23] * 3),
        reset_1=[lambda x: x[0], lambda x: x[1], lambda x: x[2]],
        reset_2=[lambda x: x[0], lambda x: x[1], lambda x: x[2]],
        f_1=[lambda x: -x[1], lambda x: -x[0] + x[2], lambda x: x[0] + (2 * x[1] + 3 * x[2]) * (1 + x[2] ** 2)],
        f_2=[lambda x: -x[1], lambda x: -x[0] + x[2], lambda x: -x[0] - 2 * x[1] - 3 * x[2]],
        name='H4'  # Safety Verification of Nonlinear Hybrid Systems Based on Bilinear Programming->H2
    ),
    5: Example(
        n=2,
        local_1=Zone(shape='box', low=[-2] * 2, up=[2] * 2),
        init=Zone(shape='ball', center=[1.125, 0.625], r=0.0125),
        unsafe=Zone(shape='ball', center=[0.875, 0.125], r=0.0125),
        f_1=[
            lambda x: x[0],
            lambda x: x[1]
        ],
        name='C1',
        continuous=True
    ),
    6: Example(
        n=2,
        local_1=Zone(shape='box', low=[-2] * 2, up=[2] * 2),
        init=Zone(shape='ball', center=[-1, 0.5], r=0.4 ** 2),
        unsafe=Zone(shape='ball', center=[-1, -0.5], r=0.4 ** 2),
        f_1=[
            lambda x: -2 * x[1],
            lambda x: x[0] ** 2
        ],
        name='C2',
        continuous=True
    ),
    7: Example(
        n=2,
        local_1=Zone(shape='box', low=[-2, -2], up=[2, 2]),
        init=Zone(shape='box', low=[0, 1], up=[1, 2]),
        unsafe=Zone(shape='box', low=[-2, -0.75], up=[-0.5, 0.75]),
        f_1=[
            lambda x: x[1] + 2 * x[0] * x[1],
            lambda x: -x[0] - x[1] ** 2 + 2 * x[0] ** 2
        ],
        name='C3',
        continuous=True
    ),
    8: Example(
        n=2,
        local_1=Zone(shape='box', low=[-2] * 2, up=[2] * 2),
        init=Zone(shape='box', low=[-1 / 4, 3 / 4], up=[1 / 4, 3 / 2]),
        unsafe=Zone(shape='box', low=[1, 1], up=[2, 2]),
        f_1=[
            lambda x: - x[0] + 2 * (x[0] ** 2) * x[1],
            lambda x: -x[1]
        ],
        name='C4',
        continuous=True
    ),
    9: Example(
        n=2,
        local_1=Zone(shape='box', low=[-3.5, -2], up=[2, 1]),
        init=Zone(shape='box', low=[1, -0.5], up=[2, 0.5]),
        unsafe=Zone(shape='box', low=[-1.4, -1.4], up=[-0.6, -0.6]),
        f_1=[
            lambda x: x[1],
            lambda x: -x[0] - x[1] + 1 / 3.0 * x[0] ** 3
        ],
        name='C5',
        continuous=True
    ),
    10: Example(
        n=2,
        local_1=Zone(shape='box', low=[-2] * 2, up=[2] * 2),
        init=Zone(shape='ball', center=[0, 0.5], r=0.2 ** 2),
        unsafe=Zone(shape='ball', center=[-1.5, -1.5], r=0.5 ** 2),
        f_1=[
            lambda x: -x[0] + 2 * (x[0] ** 3) * x[1] ** 2,
            lambda x: -x[1],
        ],
        name='C6',
        continuous=True
    ),
    11: Example(
        n=3,
        local_1=Zone(shape='box', low=[-20] * 3, up=[20] * 3),
        init=Zone(shape='ball', center=[-14.5, -14.5, 12.5], r=0.5 ** 2),
        unsafe=Zone(shape='ball', center=[-16.5, -14.5, 2.5], r=0.5 ** 2),
        f_1=[
            lambda x: 10.0 * (-x[0] + x[1]),
            lambda x: -x[1] + x[0] * (28.0 - x[2]),
            lambda x: x[0] * x[1] - 8 / 3 * x[2]
        ],
        name='C7',
        continuous=True
    ),
    12: Example(
        n=3,
        local_1=Zone(shape='box', low=[-2] * 3, up=[2] * 3),
        init=Zone(shape='ball', center=[0, 0, 0], r=1 ** 2),
        unsafe=Zone(shape='ball', center=[1.5, 1.5, 1.5], r=0.5 ** 2),
        # 非安全区域改动
        f_1=[
            lambda x: -x[0] + x[1] - x[2],
            lambda x: -x[0] * (x[2] + 1) - x[1],
            lambda x: 0.76524 * x[0] - 4.7037 * x[2]
        ],
        name='C8',
        continuous=True
    ),
    13: Example(
        n=3,
        local_1=Zone(shape='box', low=[-2] * 3, up=[2] * 3),
        init=Zone(shape='ball', center=[0.25, 0.25, 0.25], r=0.5 ** 2),
        unsafe=Zone(shape='ball', center=[1.5, -1.5, -1.5], r=0.5 ** 2),
        f_1=[
            lambda x: -x[1],
            lambda x: -x[2],
            lambda x: -x[0] - 2 * x[1] - x[2] + x[0] ** 3
        ],
        name='C9',
        continuous=True
    ),
    14: Example(
        n=4,
        local_1=Zone(shape='box', low=[-2.5] * 4, up=[2] * 4),
        init=Zone(shape='box', low=[0.5] * 4, up=[1.5] * 4),
        unsafe=Zone(shape='box', low=[-2.4] * 4, up=[-1.6] * 4),
        f_1=[
            lambda x: x[0],
            lambda x: x[1],
            lambda x: x[2],
            lambda x: - 3980 * x[3] - 4180 * x[2] - 2400 * x[1] - 576 * x[0]
        ],
        name='C10',
        continuous=True
    ),
    15: Example(
        n=4,
        local_1=Zone(shape='box', low=[-1.5] * 4, up=[1.5] * 4),
        init=Zone(shape='box', low=[-0.2, -1.2, -1.5, -1.5],
                  up=[0.2, -0.8, 1.5, 1.5]),
        unsafe=Zone(shape='box', low=[-1.2, -0.2, -1.5, -1.5],
                    up=[-0.8, 0.2, 1.5, 1.5]),
        f_1=[
            lambda x: -0.5 * x[0] ** 2 - 2 * (x[1] ** 2 + x[2] ** 2 - x[3] ** 2),
            lambda x: -x[0] * x[1] - 1,
            lambda x: -x[0] * x[2],
            lambda x: -x[0] * x[3]
        ],
        name='C11',
        continuous=True
    ),
    16: Example(
        n=6,
        local_1=Zone(shape='box', low=[-2] * 6, up=[2] * 6),
        init=Zone(shape='box', low=[0.5] * 6, up=[1.5] * 6),
        unsafe=Zone(shape='box', low=[-2] * 6, up=[-1.6] * 6),
        f_1=[
            lambda x: x[1],
            lambda x: x[2],
            lambda x: x[3],
            lambda x: x[4],
            lambda x: x[5],
            lambda x: - 800 * x[5] - 2273 * x[4] - 3980 * x[3] - 4180 * x[2] - 2400 * x[1] - 576 * x[0]
        ],
        name='C12',
        continuous=True
    ),
    17: Example(
        n=6,
        local_1=Zone(shape='box', low=[-2] * 6, up=[2] * 6),
        init=Zone(shape='box', low=[1] * 6, up=[2] * 6),
        unsafe=Zone(shape='box', low=[-1] * 6, up=[-0.5] * 6),
        f_1=[
            lambda x: x[0] * x[2],
            lambda x: x[0] * x[4],
            lambda x: (x[3] - x[2]) * x[2] - 2 * x[4] * x[4],
            lambda x: -(x[3] - x[2]) ** 2 - x[0] * x[0] + x[5] * x[5],
            lambda x: x[1] * x[5] + (x[2] - x[3]) * x[4],
            lambda x: 2 * x[1] * x[4] - x[2] * x[5],
        ],
        name='C13',
        continuous=True
    ),
    18: Example(
        n=6,
        local_1=Zone(shape='box', low=[0] * 6, up=[10] * 6),
        init=Zone(shape='box', low=[3] * 6, up=[3.1] * 6),
        unsafe=Zone(shape='box', low=[4, 4.1, 4.2, 4.3, 4.4, 4.5], up=[4.1, 4.2, 4.3, 4.4, 4.5, 4.6]),
        f_1=[
            lambda x: -x[0] ** 3 + 4 * x[1] ** 3 - 6 * x[2] * x[3],
            lambda x: -x[0] - x[1] + x[4] ** 3,
            lambda x: x[0] * x[3] - x[2] + x[3] * x[5],
            lambda x: x[0] * x[2] + x[2] * x[5] - x[3] ** 3,
            lambda x: -2 * x[1] ** 3 - x[4] + x[5],
            lambda x: -3 * x[2] * x[3] - x[4] ** 3 - x[5],
        ],
        name='C14',
        continuous=True
    ),
    19: Example(
        n=7,
        local_1=Zone(shape='box', low=[-2] * 7, up=[2] * 7),
        init=Zone(shape='ball', center=[1, 1, 1, 1, 1, 1, 1], r=0.01 ** 2),
        unsafe=Zone(shape='ball', center=[1.9, 1.9, 1.9, 1.9, 1.9, 1.9, 1.9], r=0.1 ** 2),
        f_1=[
            lambda x: -0.4 * x[0] + 5 * x[2] * x[3],
            lambda x: 0.4 * x[0] - x[1],
            lambda x: x[1] - 5 * x[2] * x[3],
            lambda x: 5 * x[4] * x[5] - 5 * x[2] * x[3],
            lambda x: -5 * x[4] * x[5] + 5 * x[2] * x[3],
            lambda x: 0.5 * x[6] - 5 * x[4] * x[5],
            lambda x: -0.5 * x[6] + 5 * x[4] * x[5],
        ],
        name='C15',
        continuous=True
    ),
    20: Example(
        n=8,
        local_1=Zone(shape='box', low=[-2] * 8, up=[2] * 8),
        init=Zone(shape='box', low=[0.5] * 8, up=[1.5] * 8),
        unsafe=Zone(shape='box', low=[-2] * 8, up=[-1.6] * 8),
        f_1=[
            lambda x: x[1],
            lambda x: x[2],
            lambda x: x[3],
            lambda x: x[4],
            lambda x: x[5],
            lambda x: x[6],
            lambda x: x[7],
            lambda x: -20 * x[7] - 170 * x[6] - 800 * x[5] - 2273 * x[4] - 3980 * x[3] - 4180 * x[2] - 2400 * x[
                1] - 576 * x[0]
        ],
        name='C16',
        continuous=True
    ),
    21: Example(
        n=9,
        local_1=Zone(shape='box', low=[-2] * 9, up=[2] * 9),
        init=Zone(shape='ball', center=[1, 1, 1, 1, 1, 1, 1, 1, 1], r=0.1 ** 2),
        unsafe=Zone(shape='ball', center=[1.9, 1.9, 1.9, 1.9, 1.9, 1.9, 1.9, 1.9, 1.9], r=0.1 ** 2),
        f_1=[
            lambda x: 3 * x[2] - x[0] * x[5],
            lambda x: x[3] - x[1] * x[5],
            lambda x: x[0] * x[5] - 3 * x[2],
            lambda x: x[1] * x[5] - x[3],
            lambda x: 3 * x[2] + 5 * x[0] - x[4],
            lambda x: 5 * x[4] + 3 * x[2] + x[3] - x[5] * (x[0] + x[1] + 2 * x[7] + 1),
            lambda x: 5 * x[3] + x[1] - 0.5 * x[6],
            lambda x: 5 * x[6] - 2 * x[5] * x[7] + x[8] - 0.2 * x[7],
            lambda x: 2 * x[5] * x[7] - x[8],
        ],
        name='C17',
        continuous=True
    ),
    22: Example(
        n=12,
        local_1=Zone(shape='box', low=[-2] * 12, up=[2] * 12),
        init=Zone(shape='ball', center=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], r=0.1 ** 2),
        unsafe=Zone(shape='ball', center=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], r=0.1 ** 2),
        f_1=[
            lambda x: x[3],
            lambda x: x[4],
            lambda x: x[5],
            lambda x: -7253.4927 * x[0] + 1936.3639 * x[10] - 1338.7624 * x[3] + 1333.3333 * x[7],
            lambda x: -7253.4927 * x[1] - 1936.3639 * x[9] - 1338.7624 * x[4] + 1333.3333 * x[6],
            lambda x: -769.2308 * x[2] - 770.2301 * x[5],
            lambda x: x[9],
            lambda x: x[10],
            lambda x: x[11],
            lambda x: 9.81 * x[1],
            lambda x: -9.81 * x[0],
            lambda x: -16.3541 * x[11] - 15.3846 * x[8]
        ],
        name='C18',
        continuous=True
    ),
    23: Example(
        n=13,
        local_1=Zone(shape='box', low=[-0.3] * 13, up=[0.3] * 13),
        init=Zone(shape='box', low=[-0.3, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2],
                  up=[0, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]),
        unsafe=Zone(shape='box', low=[-0.2, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3],
                    up=[-0.15, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25]),
        f_1=[
            lambda x: (x[1] + x[2] + x[2] + x[3] + x[3] + x[4] + x[4] + x[5] + x[5] + x[6] + x[6] + x[7]) / 100 + 1,
            lambda x: x[2],
            lambda x: -10 * (x[1] - x[1] ** 3 / 6) - x[1],
            lambda x: x[4],
            lambda x: -10 * (x[3] - x[3] ** 3 / 6) - x[1],
            lambda x: x[6],
            lambda x: -10 * (x[5] - x[5] ** 3 / 6) - x[1],
            lambda x: x[8],
            lambda x: -10 * (x[7] - x[7] ** 3 / 6) - x[1],
            lambda x: x[10],
            lambda x: -10 * (x[9] - x[9] ** 3 / 6) - x[1],
            lambda x: x[12],
            lambda x: -10 * (x[11] - x[11] ** 3 / 6) - x[1],
        ],
        name='C19',
        continuous=True
    ),
    24: Example(
        n=15,
        local_1=Zone(shape='box', low=[-0.3] * 15, up=[0.3] * 15),
        init=Zone(shape='box',
                  low=[-0.3, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2],
                  up=[0, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]),
        unsafe=Zone(shape='box',
                    low=[-0.2, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3],
                    up=[-0.15, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25,
                        -0.25, -0.25]),
        f_1=[
            lambda x: (x[1] + x[2] + x[2] + x[3] + x[3] + x[4] + x[4] + x[5] + x[5] + x[6] + x[6] + x[7] + x[7] + x[
                8]) / 100 + 1,
            lambda x: x[2],
            lambda x: -10 * (x[1] - x[1] ** 3 / 6) - x[1],
            lambda x: x[4],
            lambda x: -10 * (x[3] - x[3] ** 3 / 6) - x[1],
            lambda x: x[6],
            lambda x: -10 * (x[5] - x[5] ** 3 / 6) - x[1],
            lambda x: x[8],
            lambda x: -10 * (x[7] - x[7] ** 3 / 6) - x[1],
            lambda x: x[10],
            lambda x: -10 * (x[9] - x[9] ** 3 / 6) - x[1],
            lambda x: x[12],
            lambda x: -10 * (x[11] - x[11] ** 3 / 6) - x[1],
            lambda x: x[14],
            lambda x: -10 * (x[13] - x[13] ** 3 / 6) - x[1],
        ],
        name='C20',
        continuous=True
    ),
    25: Example(
        n=17,
        local_1=Zone(shape='box', low=[-0.3] * 17, up=[0.3] * 17),
        init=Zone(shape='box',
                  low=[-0.3, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2,
                       -0.2], up=[0, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]),
        unsafe=Zone(shape='box',
                    low=[-0.2, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3,
                         -0.3],
                    up=[-0.15, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25,
                        -0.25, -0.25, -0.25, -0.25]),
        f_1=[
            lambda x: (x[1] + x[2] + x[2] + x[3] + x[3] + x[4] + x[4] + x[5] + x[5] + x[6] + x[6] + x[7] + x[7] + x[8] +
                       x[8] + x[9]) / 100 + 1,
            lambda x: x[2],
            lambda x: -10 * (x[1] - x[1] ** 3 / 6) - x[1],
            lambda x: x[4],
            lambda x: -10 * (x[3] - x[3] ** 3 / 6) - x[1],
            lambda x: x[6],
            lambda x: -10 * (x[5] - x[5] ** 3 / 6) - x[1],
            lambda x: x[8],
            lambda x: -10 * (x[7] - x[7] ** 3 / 6) - x[1],
            lambda x: x[10],
            lambda x: -10 * (x[9] - x[9] ** 3 / 6) - x[1],
            lambda x: x[12],
            lambda x: -10 * (x[11] - x[11] ** 3 / 6) - x[1],
            lambda x: x[14],
            lambda x: -10 * (x[13] - x[13] ** 3 / 6) - x[1],
            lambda x: x[16],
            lambda x: -10 * (x[15] - x[15] ** 3 / 6) - x[1],
        ],
        name='C21',
        continuous=True
    ),

    26: Example(
        n=19,
        local_1=Zone(shape='box', low=[-0.3] * 19, up=[0.3] * 19),
        init=Zone(shape='box',
                  low=[-0.3, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2,
                       -0.2, -0.2, -0.2],
                  up=[0, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]),
        unsafe=Zone(shape='box',
                    low=[-0.2, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3,
                         -0.3, -0.3, -0.3],
                    up=[-0.15, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25,
                        -0.25, -0.25, -0.25, -0.25, -0.25, -0.25]),
        f_1=[
            lambda x: (x[1] + x[2] + x[2] + x[3] + x[3] + x[4] + x[4] + x[5] + x[5] + x[6] + x[6] + x[7] + x[7] + x[8] +
                       x[8] + x[9] + x[9] + x[10]) / 100 + 1,
            lambda x: x[2],
            lambda x: -10 * (x[1] - x[1] ** 3 / 6) - x[1],
            lambda x: x[4],
            lambda x: -10 * (x[3] - x[3] ** 3 / 6) - x[1],
            lambda x: x[6],
            lambda x: -10 * (x[5] - x[5] ** 3 / 6) - x[1],
            lambda x: x[8],
            lambda x: -10 * (x[7] - x[7] ** 3 / 6) - x[1],
            lambda x: x[10],
            lambda x: -10 * (x[9] - x[9] ** 3 / 6) - x[1],
            lambda x: x[12],
            lambda x: -10 * (x[11] - x[11] ** 3 / 6) - x[1],
            lambda x: x[14],
            lambda x: -10 * (x[13] - x[13] ** 3 / 6) - x[1],
            lambda x: x[16],
            lambda x: -10 * (x[15] - x[15] ** 3 / 6) - x[1],
            lambda x: x[18],
            lambda x: -10 * (x[17] - x[17] ** 3 / 6) - x[1],
        ],
        name='C22',
        continuous=True
    ),
    27: Example(
        n=21,
        local_1=Zone(shape='box', low=[-0.3] * 21, up=[0.3] * 21),
        init=Zone(shape='box',
                  low=[-0.3, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2,
                       -0.2, -0.2, -0.2, -0.2, -0.2],
                  up=[0, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
                      0.3]),
        unsafe=Zone(shape='box',
                    low=[-0.2, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3,
                         -0.3, -0.3, -0.3, -0.3, -0.3],
                    up=[-0.15, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25,
                        -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25]),
        f_1=[
            lambda x: (x[1] + x[2] + x[2] + x[3] + x[3] + x[4] + x[4] + x[5] + x[5] + x[6] + x[6] + x[7] + x[7] + x[8] +
                       x[8] + x[9] + x[9] + x[10] + x[10] + x[11]) / 100 + 1,
            lambda x: x[2],
            lambda x: -10 * (x[1] - x[1] ** 3 / 6) - x[1],
            lambda x: x[4],
            lambda x: -10 * (x[3] - x[3] ** 3 / 6) - x[1],
            lambda x: x[6],
            lambda x: -10 * (x[5] - x[5] ** 3 / 6) - x[1],
            lambda x: x[8],
            lambda x: -10 * (x[7] - x[7] ** 3 / 6) - x[1],
            lambda x: x[10],
            lambda x: -10 * (x[9] - x[9] ** 3 / 6) - x[1],
            lambda x: x[12],
            lambda x: -10 * (x[11] - x[11] ** 3 / 6) - x[1],
            lambda x: x[14],
            lambda x: -10 * (x[13] - x[13] ** 3 / 6) - x[1],
            lambda x: x[16],
            lambda x: -10 * (x[15] - x[15] ** 3 / 6) - x[1],
            lambda x: x[18],
            lambda x: -10 * (x[17] - x[17] ** 3 / 6) - x[1],
            lambda x: x[20],
            lambda x: -10 * (x[19] - x[19] ** 3 / 6) - x[1],
        ],
        name='C23',
        continuous=True
    ),
    28: Example(
        n=23,
        local_1=Zone(shape='box', low=[-0.3] * 23, up=[0.3] * 23),
        init=Zone(shape='box',
                  low=[-0.3, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2,
                       -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2],
                  up=[0, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
                      0.3, 0.3, 0.3]),
        unsafe=Zone(shape='box',
                    low=[-0.2, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3,
                         -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3],
                    up=[-0.15, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25,
                        -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25]),
        f_1=[
            lambda x: (x[1] + x[2] + x[2] + x[3] + x[3] + x[4] + x[4] + x[5] + x[5] + x[6] + x[6] + x[7] + x[7] + x[8] +
                       x[8] + x[9] + x[9] + x[10] + x[10] + x[11] + x[11] + x[12]) / 100 + 1,
            lambda x: x[2],
            lambda x: -10 * (x[1] - x[1] ** 3 / 6) - x[1],
            lambda x: x[4],
            lambda x: -10 * (x[3] - x[3] ** 3 / 6) - x[1],
            lambda x: x[6],
            lambda x: -10 * (x[5] - x[5] ** 3 / 6) - x[1],
            lambda x: x[8],
            lambda x: -10 * (x[7] - x[7] ** 3 / 6) - x[1],
            lambda x: x[10],
            lambda x: -10 * (x[9] - x[9] ** 3 / 6) - x[1],
            lambda x: x[12],
            lambda x: -10 * (x[11] - x[11] ** 3 / 6) - x[1],
            lambda x: x[14],
            lambda x: -10 * (x[13] - x[13] ** 3 / 6) - x[1],
            lambda x: x[16],
            lambda x: -10 * (x[15] - x[15] ** 3 / 6) - x[1],
            lambda x: x[18],
            lambda x: -10 * (x[17] - x[17] ** 3 / 6) - x[1],
            lambda x: x[20],
            lambda x: -10 * (x[19] - x[19] ** 3 / 6) - x[1],
            lambda x: x[22],
            lambda x: -10 * (x[21] - x[21] ** 3 / 6) - x[1],
        ],
        name='C24',
        continuous=True
    )
}


def get_example_by_id(id: int):
    return examples[id]


def get_example_by_name(name: str):
    for ex in examples.values():
        if ex.name == name:
            return ex
    raise ValueError('The example {} was not found.'.format(name))
