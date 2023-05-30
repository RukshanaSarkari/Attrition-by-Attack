import streamlit as st
import pandas as pd

df = pd.read_csv(r"Attrition by Attack (Updated).csv")
pd.set_option("display.max_columns", None)

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

if design_point:
    st.write(df.loc[:,["design_point"]])
if iteration:
    st.write(df.loc[:, ["iteration"]])
if scenarioID:
    st.write(df.loc[:, ["ScenarioId"]])
if iterationID:
    st.write(df.loc[:, ["IterationId"]])
if attackName:
    st.write(df.loc[:, ["porthosAttackName"]])
if timeAttack:
    st.write(df.loc[:, ["time"]])
if airbase:
    st.write(df.loc[:, ["AirbaseId"]])
if pEntity:
    st.write(df.loc[:, ["porthosEntityId"]])
if aEntity:
    st.write(df.loc[:, ["athosEntityId"]])
if typeName:
    st.write(df.loc[:, ["entityTypeName"]])
if name:
    st.write(df.loc[:, ["EntityName"]])
if cEntity:
    st.write(df.loc[:, ["containedEntityName"]])
if kCriteria:
    st.write(df.loc[:, ["killCriteria"]])
if kCriteriaAchieved:
    st.write(df.loc[:, ["KillCriteriaAchieved"]])

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