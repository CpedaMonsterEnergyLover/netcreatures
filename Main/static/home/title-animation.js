$(document).ready(function() {
    // Existing code for question and news animation
    $('.question').on('click', function() {
        $(this).next('.answer').slideToggle();
    });

    $('.news-container').animate({scrollLeft: '+=500'}, 5000);

    // New animation for titles
    function animateTitles() {
        $('h1, h2').each(function() {
            const title = $(this);
            const text = title.text();
            title.empty();
            title.css({'visibility': 'visible'})
            // Create RGB spans
            const colors = ['cyan', 'blue', 'magenta', 'red', 'yellow', 'green'];
            colors.forEach((color) => {
                const span = $('<span>').text(text).css({
                    'position': 'absolute',
                    'left': '50%', // Center horizontally
                    'transform': 'translate(-50%, -100%)', // Correct centering
                    'color': color,
                    'mix-blend-mode': 'screen',
                    'pointer-events': 'none',
                    'text-wrap': 'nowrap',
                    'font-weight': 'bold'
                });
                title.append(span);
            });

            let currentMousePos = { x: $(window).width() + 200, y: $(window).height() + 200 };
            let currentScroll = { x: 0, y: 0 };

            $(document).mousemove(function(event) {
                currentMousePos.x = event.pageX;
                currentMousePos.y = event.pageY;
            });

            $(window).scroll(function(event) {
                if (currentScroll.x !== $(document).scrollLeft()) {
                    currentMousePos.x -= currentScroll.x;
                    currentScroll.x = $(document).scrollLeft();
                    currentMousePos.x += currentScroll.x;
                }
                if (currentScroll.y !== $(document).scrollTop()) {
                    currentMousePos.y -= currentScroll.y;
                    currentScroll.y = $(document).scrollTop();
                    currentMousePos.y += currentScroll.y;
                }
            });

            function animation() {
                const titleOffset = title.offset();
                const titleCenterX = titleOffset.left + title.width() / 2;
                const titleCenterY = titleOffset.top + title.height() / 2;

                const distanceX = currentMousePos.x - titleCenterX;
                const distanceY = currentMousePos.y - titleCenterY;

                const maxOffset = 200; // Maximum offset
                const minDistance = 200;
                const reqDistance = 1000;
                let distance = Math.sqrt(distanceX * distanceX + distanceY * distanceY) - minDistance;
                if (distance < 0) distance = 0
                else if (distance > reqDistance) return
                const scale = Math.min(distance / 1000, 1); // Scale based on distance
                const offset = maxOffset * Math.pow(scale, 2); // Quadratic scaling of the offset

                // Set offsets and blur for each span
                title.children('span').each(function(index) {
                    const angle = (index * (2 * Math.PI / colors.length)) + Math.atan2(distanceY, distanceX);
                    const offsetX = -Math.cos(angle) * offset; // Move in the opposite direction of the mouse
                    const offsetY = -Math.sin(angle) * offset;

                    // Blur effect based on offset
                    const blurAmount = offset * 0.33; // Adjust this divisor for more/less blur sensitivity

                    $(this).css({
                        'transform': `translate(-50%, -100%) translate(${offsetX}px, ${offsetY}px)`,
                        'filter': `blur(${blurAmount}px)`,
                    }); // Keep centered and apply blur
                });
            }

            animation()

            $(document).on('mousemove', animation);
            $(window).on('scroll', animation);
        });
    }

    animateTitles(); // Call the function to start the animation
});

