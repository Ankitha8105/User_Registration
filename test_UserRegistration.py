'''
    @Author: Ankitha
    @Date: 21-11-2024
    @Last Modified by: Ankitha
    @Last Modified time: 21-11-2024
    @Title : File to test input details

'''
import pytest
import UserRegistration


@pytest.mark.parametrize("fname,expected",[("Ankitha",True),('Pooja',True),('An',False),('someone',False)])
def test_fname_valid(fname,expected):
    assert UserRegistration.valid_firstname(fname) == expected