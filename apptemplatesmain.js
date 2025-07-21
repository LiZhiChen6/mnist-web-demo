document.getElementById('upload-form').onsubmit = async function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    const res = await fetch('/predict', {
        method: 'POST',
        body: formData
    });
    const data = await res.json();
    if(data.prediction !== undefined) {
        document.getElementById('result').innerText = '识别结果：' + data.prediction;
    } else {
        document.getElementById('result').innerText = '识别失败：' + (data.error || '未知错误');
    }
};
