"""mask_functions.py

A collection of functions to make masks on data.
See test_* functions in this directory for nose tests
"""
from __future__ import print_function, division

import sys, os, pdb
import numpy as np
import nibabel as nib
import numpy.linalg as npl

from os.path import splitext
from numpy.testing import assert_array_equal
from scipy.ndimage import affine_transform


def make_mask_filtered_data(func_path, mask_path):
    """Return the masked filtered data

    Parameters
    ----------
    func_path: string
    	  path to the 4D data
    
    mask_path: string
        path to the mask function

    Return
    ------
    masked_func: 4D array
        masked filtered data
    
    """
    func_img = nib.load(func_path)
    mask_img = nib.load(mask_path)
    mask = mask_img.get_data()
    func_data = func_img.get_data()
    # Make data 4D to prepare for "broadcasting"
    mask = np.reshape(mask, mask.shape + (1,))
    # "Broadcasting" expands the final length 1 dimension to match the func data
    masked_func = nib.Nifti1Image(func_data, func_img.affine, func_img.header)
    # nib.save(masked_func, 'masked_' + img_name )
    return masked_func

def resample_filtered_data(func_path, template_path):
    """Resample template to filtered functional dataset
    
    Parameters
    ----------
    func_path: string
        path of the 4D filtered data to resample
    template_path: string
        path to the template to apply on the data
    
    """
    filtered_func = nib.load(func_path) 
    filtered_shape = filtered_func.shape[:3]
    template_img = nib.load(mni_fname)
    template_data = template_img.get_data()
    vox2vox = npl.inv(template_img.affine).dot(filtered_func.affine)
    M, trans = nib.affines.to_matvec(vox2vox)
    resampled = affine_transform(template_data, M, trans,
                                 output_shape=filtered_shape)
    froot, ext = splitext(mni_fname)
    new_name = froot + '_2mm' + ext
    new_img = nib.Nifti1Image(resampled, filtered_func.affine,
                              template_img.header)
    #nib.save(new_img, new_name) 
    return new_img
