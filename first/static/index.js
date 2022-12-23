const itemselect = document.getElementById('itemselect')
const output = document.getElementById('output')

itemselect.addEventListener(
    'change', 
    event => output.value = event.target.value
)