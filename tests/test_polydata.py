import pytest
import numpy as np
import vtkInterface as vtki
from vtkInterface import examples
from vtkInterface.plotting import RunningXServer

spherefile = examples.spherefile
sphere = vtki.Sphere()
    
def test_loadfromfile():
    sphere = vtki.PolyData(spherefile)
    assert sphere.GetNumberOfPoints()
    assert sphere.GetNumberOfCells()
    assert hasattr(sphere, 'points')


def test_raytrace():
    points, ind = sphere.RayTrace([0, 0, 0], [1, 1, 1])
    assert np.any(points)
    assert np.any(ind)


@pytest.mark.skipif(not RunningXServer(), reason="Requires active X Server")
def test_plot_curvature():
    cpos = sphere.PlotCurvature(off_screen=True)
    assert isinstance(cpos, list)
