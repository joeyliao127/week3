const hamburger = document.querySelector(".hamburger");
const topItems = document.querySelector(".top-items");
const body = document.querySelector("body");
const windowWidth = window.innerWidth;
const pic_top_container = document.querySelector(".pic-top-container");
const pic_bottom_container = document.querySelector(".pic-bottom-container");
const loadMore = document.querySelector(".loadMore");
src =
  "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";

function url_maker(data) {
  const cut = data.split("https");
  const url = "https" + cut[1];
  return url;
}
let count = 0;
let spareData = [];
async function render() {
  try {
    const header = await fetch(src);
    const content = await header.json();
    let data = content.result.results;
    data.forEach((element) => {
      const { stitle, file } = element;
      let stock = [stitle, file];
      spareData.push(stock);
    });

    for (let i = 0; i < 3; i++) {
      const promotion_item = document.createElement("div");
      const promotion_item_img = document.createElement("img");
      const promotion_item_p = document.createElement("p");
      //圖片處理
      url = url_maker(data[count].file);
      promotion_item_img.setAttribute("src", url);
      promotion_item.appendChild(promotion_item_img);
      //p標籤處理
      promotion_item_p.textContent = data[count].stitle;
      promotion_item.appendChild(promotion_item_p);
      promotion_item.classList.add("promotion-item");
      pic_top_container.appendChild(promotion_item);
      count += 1;
    }
    for (let i = 0; i < 12; i++) {
      const title_item = document.createElement("div");
      const titel_item_img = document.createElement("img");
      const text = document.createElement("div");
      const text_p = document.createElement("p");
      //處理文字
      text.classList.add("text");
      text_p.textContent = data[count].stitle;
      text.appendChild(text_p);
      //title_item_img處理
      url = url_maker(data[count].file);
      titel_item_img.setAttribute("src", url);
      //插入titel_item
      title_item.classList.add("title-item");
      title_item.appendChild(titel_item_img);

      title_item.appendChild(text);
      //插入到pic-bottom-container
      pic_bottom_container.appendChild(title_item);

      count += 1;
    }
  } catch (e) {
    console.log(e);
  }
}

render();
//等待spareData儲存到全域變數
setTimeout(() => {
  console.log(spareData);
}, 1000);

try {
  loadMore.addEventListener("click", () => {
    for (let i = 0; i < 12; i++) {
      if (count < spareData.length) {
        const title_item = document.createElement("div");
        const titel_item_img = document.createElement("img");
        const text = document.createElement("div");
        const text_p = document.createElement("p");
        //處理文字
        text.classList.add("text");
        text_p.textContent = spareData[count][0];
        text.appendChild(text_p);
        //title_item_img處理
        url = url_maker(spareData[count][1]);
        titel_item_img.setAttribute("src", url);
        //插入titel_item
        title_item.classList.add("title-item");
        title_item.appendChild(titel_item_img);
        title_item.appendChild(text);
        //插入到pic-bottom-container
        pic_bottom_container.appendChild(title_item);

        count += 1;
      } else {
        console.log("關閉loadMore");
        loadMore.style.display = "none";
      }
    }
  });
} catch (e) {
  console.log("Button Event錯誤");
  console.log(e);
}

//week1
// hamburger.addEventListener("click", (e) => {
//   e.stopPropagation();
//   topItems.style.display = "block";
//   body.classList.add("no-scroll");
//   body.style.overflow = "hidden";
// });

// body.addEventListener("click", (e) => {
//   if (windowWidth > 360 && windowWidth < 600) {
//     console.log("window click event");
//     if (!e.target.closest(".hamburger")) {
//       body.classList.remove("no-scroll");
//       body.style.overflow = "auto";
//     }
//     topItems.style.display = "none";
//   }
// });

// topItems.addEventListener("click", (e) => {
//   e.stopPropagation();
//   topItems.style.display = "block";
// });
