# caviar-annotation-to-yolo-annotation
<grouplist>
<context evaluation="1.0">fighting</context>
<situation evaluation="1.0">fighting</situation>


walking - 0
immobile - 1
meeting - 2
browsing - 3
fighting - 4
dropdown - 5

<context evaluation="1.0">walking</context>
<context evaluation="1.0">immobile</context> - Removed - 3rd XML

<context evaluation="1.0">drop down</context> - Rest_FallOnFloor
<situation evaluation="1.0">inactive</situation>

<context evaluation="1.0">immobile</context> - Rest_InChair
<situation evaluation="1.0">inactive</situation>

<context evaluation="1.0">drop down</context> - Rest_SlumpOnFloor
<situation evaluation="1.0">inactive</situation>

<context evaluation="1.0">drop down</context> - Rest_WiggleOnFloor
<situation evaluation="1.0">inactive</situation>



<context evaluation="1.0">walking</context> - Meet Crowd
<situation evaluation="1.0">moving</situation>

<context evaluation="1.0">meeting</context> - Meet_Split_3rdGuy


<context evaluation="1.0">leaving</context> - Leaving







<movement evaluation="1.0">active</movement>
<role evaluation="1.0">browser</role>
<context evaluation="1.0">browsing</context>
<situation evaluation="1.0">browsing</situation>

Browse_WhileWaiting1 - Excluded due to immobile