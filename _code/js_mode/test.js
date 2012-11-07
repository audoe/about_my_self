function tabsShowHide (e) {
    //更新标签栏
	var area = $(this).closest("div");
	area.find("li").removeClass("sellected");
	$(this).closest("li").addClass("sellected");
    //替换body内容
	var class_name = $(this).attr("class");
	var body = area.find("div.tabBody");
	body.addClass("hidden");
	var targe = area.find("div."+class_name);
	if (targe){
		targe.removeClass("hidden");
	}

}
