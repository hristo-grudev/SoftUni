function create(words) {
   const content = document.getElementById('content');
   content.addEventListener('click', reveal);

   for (let word of words){
      const div = document.createElement('div');
      const para = document.createElement('p');

      para.textContent = word;
      para.style.display = 'none';
      div.appendChild(para);

      div.addEventListener('click', reveal);
      content.appendChild(div);      
   }
   function reveal(e) {
      if (e.target.tagNme == 'DIV' && e.target != content){
      e.currentTarget.children[0].style.display = '';
      }
   }
}
