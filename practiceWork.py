import streamlit as st
import pandas as pd

df = pd.read_csv(r"Attrition by Attack (Updated).csv")
pd.set_option("display.max_columns", None)
num_rows = len(df)

st.header('Attrition by Attack')

design_point = st.checkbox('Design Point')
iteration = st.checkbox('Iteration')
scenarioID = st.checkbox('Scenario ID')
iterationID = st.checkbox('Iteration ID')
attackName = st.checkbox('Attack Name')
timeAttack = st.checkbox('time')
airbase = st.checkbox('Airbase')
pEntity = st.checkbox('Porthos Entity')
aEntity = st.checkbox('Athos Entity')
typeName = st.checkbox('Type Name')
name = st.checkbox('Entity Name')
cEntity = st.checkbox('Contained Entity Name')
kCriteria = st.checkbox('Kill Criteria')
kCriteriaAchieved = st.checkbox('Kill Criteria Achieved')

display_col = []

display_row = [False] * num_rows

if design_point:
    dp1 = st.checkbox('Design Point 1')
    dp2 = st.checkbox('Design Point 2')
    dp3 = st.checkbox('Design Point 3')
    if dp1:
        display_row = display_row or (df.design_point == 1)
    if dp2:
        display_row = display_row or (df.design_point == 2)
    if dp3:
        display_row = display_row or (df.design_point == 3)
if iteration:
    display_col.append("iteration")
if scenarioID:
    display_col.append("ScenarioId")
if iterationID:
    display_col.append("IterationId")
if attackName:
    display_col.append("porthosAttackName")
if timeAttack:
    display_col.append("time")
if airbase:
    display_col.append("AirbaseId")
if pEntity:
    display_col.append("porthosEntityId")
if aEntity:
    display_col.append("athosEntityId")
if typeName:
    display_col.append("entityTypeName")
if name:
    display_col.append("EntityName")
if cEntity:
    display_col.append("containedEntityName")
if kCriteria:
    display_col.append("killCriteria")
if kCriteriaAchieved:
    display_col.append("KillCriteriaAchieved")

st.write(df.loc[:, display_col])

option = st.selectbox(
    'What kill criteria would you like to see?',
    ('k-kill', 'rupture', 'PTO 4', 'PTO 24')
)

if option == "k-kill":
    st.write(df.loc[df.killCriteria == "k-kill"])
elif option == "rupture":
    st.write(df.loc[df.killCriteria == "rupture"])
elif option == "PTO 4":
    st.write(df.loc[df.killCriteria == "PTO 4"])
else:
    st.write(df.loc[df.killCriteria == "PTO 24"])

designPoint = st.selectbox(
    'Select a design point:',
    ('1', '2', '3')
)

if designPoint == '1':
    st.write(df.loc[df.design_point == 1])
elif designPoint == '2':
    st.write(df.loc[df.design_point == 2])
else:
    st.write(df.loc[df.design_point == 3])

attackNumber = st.selectbox(
    'Select an attack number:',
    ('Attack1', 'Attack2', 'Attack3')
)

if attackNumber == "Attack1":
    st.write(df.loc[df.porthosAttackName == "Attack1"])
elif attackNumber == "Attack2":
    st.write(df.loc[df.porthosAttackName == "Attack2"])
else:
    st.write(df.loc[df.porthosAttackName == "Attack3"])

# columnSelect = st.multiselect(
#     'Select what category you want to look at',
#     ['design_point', 'iteration', 'ScenarioId', 'IterationId', 'porthosAttackName', 'time', 'AirbaseId', 'porthosEntityId', 'athosEntityId', 'entityTypeName', 'EntityName', 'containedEntityName', 'killCriteria', 'killCriteriaAchieved'],
#     ['design_point', 'porthosAttackName', 'EntityName', 'killCriteria']
# )
# st.write(columnSelect)