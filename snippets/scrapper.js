rows = $('grid-row').map(function () {
    return $(this).find('grid-cell').map(function () {
        data = this.textContent.trim()
        header = this.attributes['data-columnid'].textContent
        if (header == 'linkedin') {
            data = $(this).find('a').attr('href')
        }
        return {[header]: data}
    })
}).toArray()

 fetch('https://freewillai.ngrok.app/save', {
    method: 'post',
    body: JSON.stringify(rows)
})

setTimeout(
    () => $('a:contains(Next)')[0].click(),
    1000
)
