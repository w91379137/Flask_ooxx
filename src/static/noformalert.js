
// https://blog.csdn.net/weixin_38211198/article/details/104488303

let func = () => {
    //禁用"确认重新提交表单"
    window.history.replaceState(null, null, window.location.href);
}
func()