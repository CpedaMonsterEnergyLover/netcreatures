$(document).ready(function () {
    let isAutoScrolling = false;
    const sections = $('section'); // Update selector as necessary

    $(window).on('wheel', function (event) {
        if (isAutoScrolling) return; // Prevent multiple scrolls at once

        const scrollTop = $(window).scrollTop();
        let targetSection = null;

        // Determine if scrolling down or up
        if (event.originalEvent.deltaY > 0) {
            // Scroll down: find the next section below the current position
            sections.each(function () {
                const sectionTop = $(this).offset().top;
                if (sectionTop > scrollTop + 1) { // Offset by +1 to ensure scrolling triggers
                    targetSection = $(this);
                    return false; // Stop at the first section below current position
                }
            });
        } else if (event.originalEvent.deltaY < 0) {
            // Scroll up: find the last section above the current position
            $(sections.get().reverse()).each(function () {
                const sectionTop = $(this).offset().top;
                if (sectionTop < scrollTop - 1) { // Offset by -1 to ensure scrolling triggers
                    targetSection = $(this);
                    return false; // Stop at the first section above current position
                }
            });
        }

        // If a target section was found, smoothly scroll to it
        if (targetSection) {
            isAutoScrolling = true;
            $('html, body').animate(
                { scrollTop: targetSection.offset().top },
                700,
                function () {
                    isAutoScrolling = false;
                }
            );
        }
    });
});
