const modal = document.querySelector('#modal')
const content = document.querySelector('#modal-content')

const openModal = () => {
    modal.classList.remove('hidden')
    modal.classList.add('flex')

    setTimeout(()=>{
        content.classList.remove('opacity-50', 'scale-95')
    }, 50)
}

const closeModal = () => {
    content.classList.add('opacity-50', 'scale-95')    

    setTimeout(()=>{
        modal.classList.remove('flex')
        modal.classList.add('hidden')
    }, 200)
}


document.addEventListener('keydown', (event)=>{
    if(event.key === 'Escape') closeModal()
})

modal.addEventListener('click', (event)=>{
    if(event.target.id === 'modal') closeModal()
})

