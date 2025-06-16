function writeBtn(){
    if($(".btitle").val().length<2){
        alert('제목은 한글자 이상 입력하셔야 합니다.');
        $(".btitle").focus();
        return;
    }
    alert('게시글을 등록합니다.');
    // writeFrm.submit()
}