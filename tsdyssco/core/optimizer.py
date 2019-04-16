from .fermentation_metrics import *
from.two_stage_dfba import *
from scipy.optimize import minimize_scalar


def optimization_target(time_switch, initial_concs, time_end, two_stage_fluxes, objective_fun):
    data, time = two_stage_timecourse(initial_concs, time_end, time_switch, two_stage_fluxes)
    return -objective_fun(data, time)


def optimal_switch_time(initial_concs, time_end, two_stage_fluxes, objective_fun=batch_productivity):

    opt_result = minimize_scalar(optimization_target,
                                 args=(initial_concs, time_end, two_stage_fluxes, objective_fun),
                                 bounds=[0, time_end], options={'maxiter': 1000000}, method='brent')

    if opt_result.x <= 0:
        opt_result.x = 0
    elif opt_result.x > time_end:
        opt_result.x = time_end
    return opt_result


