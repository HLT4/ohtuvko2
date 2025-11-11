*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  jari  salasana123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  jari  moikka123
    Input New Command
    Input Credentials  jari  salasana123
    Output Should Contain  User with username jari already exists

Register With Too Short Username And Valid Password
    Input Credentials  a  salasana123
    Output Should Contain  Username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  123456  salasana123
    Output Should Contain  Username can only contain letters

Register With Valid Username And Too Short Password
    Input Credentials  jari  a
    Output Should Contain  Password is too short


Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  jari  salasana
    Output Should Contain  Password can't contain only letters