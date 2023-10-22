function selectTab(selectedTab) {
    let tabs = document.querySelectorAll('.tab');
    for (var i = 0; i < tabs.length; i++) {
        tabs[i].classList.remove("selected");
    }
    document.querySelector('.'+selectedTab).classList.add('selected');
}

function toggleActions(formId) {
    let actionCnt = document.querySelector("tr#id-"+formId + " .actions-cnt");
    if(actionCnt) {
        let show = true;
        if(actionCnt.classList.contains("dN")){
            show = false;
        }
        if(show) {
            actionCnt.classList.remove("dN");
        } else {
            actionCnt.classList.remove("dN");
        }
    }
}

