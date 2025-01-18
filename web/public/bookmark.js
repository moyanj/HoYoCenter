if (location.href === "https://user.mihoyo.com/#/account/home") {
    document.body.innerHTML = `
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 20px;
            }
            .container {
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                max-width: 600px;
                margin: 30px auto;
            }
            p {
                color: #555;
                font-size: 16px;
                white-space: pre-wrap; /* 保留换行符和空格 */
                word-wrap: break-word; /* 长单词或无法使用断点的URL强制换行 */
            }
            .button {
                color: #f8f9fa;
                display: inline-block;
                padding: 6px 8px;
                transition: background-color 300ms;
                background-color: #007bff;
                user-select:none;
                border-radius: 6px;
                box-shadow: 0px 3px 1px -2px rgba(0, 0, 0, 0.2), 0px 2px 2px 0px rgba(0, 0, 0, 0.15), 0px 1px 5px 0px rgba(0, 0, 0, 0.12);
                cursor: pointer;
                margin-top: 10px;
            }
            .button:hover {
                background-color: #0056b3;
            }
        </style>
        <div class="container">
            <h1>Cookie：</h1>
            <p id="cookie"></p>
            <br>
            <p>点击复制按钮可以复制Cookie信息。</p>
            <div class="button" id="copyButton">复制Cookie</divn>
        </div>
    `;

    let cookie = document.cookie;
    document.getElementById("cookie").textContent = cookie;

    // 复制按钮的点击事件
    document.getElementById("copyButton").addEventListener("click", function () {
        navigator.clipboard.writeText(cookie).then(() => {
            alert("Cookie已复制到剪贴板");
        }).catch(err => {
            console.error("复制失败:", err);
        });
    });
} else {
    alert("请跳转至https://user.mihoyo.com/#/account/home后再执行该脚本");
    setTimeout(() => {
        location.href = "https://user.mihoyo.com/#/account/home";
    }, 2000); // 延迟2秒跳转，给用户时间看到提示
}