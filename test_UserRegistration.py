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

@pytest.mark.parametrize("lname,expected",[("Reddy",True),('kumar',False),('Ab',False)])
def test_lname_valid(lname,expected):
    assert UserRegistration.valid_lname(lname) == expected

@pytest.mark.parametrize("email,expected",[("abc.xyz@bl.co.in",True),('.xyz@bl.co.in',False),('abc@bl.co',True)])
def test_email_valid(email,expected):
    assert UserRegistration.valid_email(email) == expected

@pytest.mark.parametrize("mobilenum,expected",[("91 9876543212",True),('098765432',False),('91 9986448691',True)])
def test_email_valid(mobilenum,expected):
    assert UserRegistration.valid_mobilenum(mobilenum) == expected

@pytest.mark.parametrize("password,expected_password",[('Thgfdcbn',True),('Hhhh58hg',False)])
def test_password_valid(password,expected_password):
    assert UserRegistration.validate_password(password) == expected_password